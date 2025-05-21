from __future__ import annotations

import argparse
import subprocess
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--cov-fail-under', type=float, default=100.0,
                        help='Fail if coverage is below this percentage')
    args, unknownargs = parser.parse_known_args(argv)

    # Check if --outputjson is already in the unknownargs
    has_output_json = any(arg.startswith('--outputjson') for arg in unknownargs)

    if has_output_json:
        # User provided their own outputjson, we'll use that
        return run_pyright_with_coverage(unknownargs, args.cov_fail_under)
    else:
        pyright_args = unknownargs + ['--outputjson']
        return_code = run_pyright_with_coverage(pyright_args, args.cov_fail_under)
        return return_code


def run_pyright_with_coverage(
        pyright_args: list[str],
        cov_fail_under: float,
    ) -> int:
    # Run pyright with the provided arguments
    result = subprocess.run(['pyright'] + pyright_args, capture_output=True, text=True)

    # Print pyright's output to maintain normal behavior
    sys.stderr.write(result.stderr)

    # Parse the JSON output if available
    data = json.loads(result.stdout)
    cov_percent = calculate_coverage_percentage(data)

    if cov_percent < cov_fail_under:
        print(f"Coverage {cov_percent:.1f}% is below minimum required {cov_fail_under:.1f}%")
        return 1
    return 0


def calculate_coverage_percentage(pyright_data: dict) -> float:
    """Calculate the percentage of typed code coverage."""
    typed = pyright_data['typeCompleteness']['completenessScore']
    return typed * 100


if __name__ == '__main__':
    sys.exit(main())
