import argparse
from typing import List
from typing import Union

from fzflib import FZF


def main() -> int:

    # CLI
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--multi",
        action="store_true",  # Default: False
        help="Mutliple selections. Default: False",
    )

    args = parser.parse_args()

    # Options
    multi: bool = args.multi

    # Logic

    fzf = FZF(multi=multi)

    result: Union[str, List[str]] = fzf.prompt()

    print(result)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
