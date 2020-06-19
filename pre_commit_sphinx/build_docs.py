import argparse
import os
from typing import Optional
from typing import Sequence


def requires_build(filenames: Sequence[str], always_build: bool) -> bool:
    """ Uses filenames list to check if anything has changed in the documentation folder.
    """
    if not always_build:
        # Always return true for now (we rebuild with breathe/exhale so source code changes also require doc build)
        # In future allow rebuild e.g. only if files in the docs directory change
        pass
    return True


def build(cache_dir: str, html_dir: str, src_dir: str):
    """ Invokes sphinx-build to build the docs
    """

    # Run Sphinx to build the documentation
    ret = os.system(f'sphinx-build -b html -d {cache_dir} {src_dir} {html_dir}')

    # It's very weird that pre-commit marks this as 'PASSED' if I return an error code 512...! Workaround:
    return 0 if ret == 0 else 1


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed',
    )
    parser.add_argument(
        '--always-build', type=bool, default=True,
        help='Always rebuild, even if no doc files have changed (useful if using \
             breathe/exhale to extract docstrings from code)',
    )
    parser.add_argument(
        '--cache-dir', type=str, default='docs/doctrees',
        help='Directory to cache doctrees for fast rebuild where there are few changes',
    )
    parser.add_argument(
        '--html-dir', type=str, default='docs/html',
        help='Directory to output the build html',
    )
    parser.add_argument(
        '--source-dir', type=str, default='docs/source',
        help='Directory containing documentation sources (where the conf.py file exists)',
    )

    args = parser.parse_args(argv)
    if requires_build(args.filenames, args.always_build):
        return build(args.cache_dir, args.html_dir, args.source_dir)

    return 0


if __name__ == '__main__':
    exit(main())
