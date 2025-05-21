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
    parser.add_argument('--fail-under', type=float, default=100.0,
                        help='Fail if coverage is below this percentage')
    args, unknownargs = parser.parse_known_args(argv)
    pyright_args = list(unknownargs)
    if '--outputjson' not in pyright_args:
        pyright_args.append('--outputjson')
    return run_pyright_with_coverage(pyright_args, args.fail_under)


def run_pyright_with_coverage(
        pyright_args: list[str],
        cov_fail_under: float,
    ) -> int:
    result = subprocess.run(['pyright', *pyright_args], capture_output=True, text=True)

    # Print pyright's output to maintain normal behavior
    sys.stderr.write(result.stderr)
    print(result.stdout)
    data = json.loads(result.stdout)
    cov_percent = calculate_coverage_percentage(data)

    if cov_percent < cov_fail_under:
        print(f"Coverage {cov_percent:.1f}% is below minimum required {cov_fail_under:.1f}%")
        return 1
    print(f"Coverage {cov_percent:.1f}% is at or above minimum required {cov_fail_under:.1f}%")
    return 0


def calculate_coverage_percentage(pyright_data: dict) -> float:
    """Calculate the percentage of typed code coverage."""
    typed = pyright_data['typeCompleteness']['completenessScore']
    return typed * 100


if __name__ == '__main__':
    sys.exit(main())
