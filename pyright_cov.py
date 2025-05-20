# usage

# you run `pyright-cov` and all other flags just go straight to pyright
# but there's an additional `--cov-fail-under`

# Ah, but we need some json file to write to, correct?
# So:
# - if outputjson is passed, use that
# - else, use temporary file
# Within the temporary file handles
#     Use subprocess to run pyright, with those flags (plus outputjson, if necessary)
#     process the output json 
# if coverage is too low, exit 1
# else, exit with pyright's code

from __future__ import annotations
from typing import Sequence
import sys

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--cov-fail-under', default=100)
    args, unknownargs = parser.parse_known_args()

    srcs = [
        str(Path(i).resolve())
        for i in args.application_directories.split(':')
    ]
    ret = 0
    for file in args.files:
        ret |= absolute_imports(
            file,
            srcs,
            never=args.never,
        )
    return ret


if __name__ == '__main__':
    main()
