import argparse
import logging
from typing import Optional
from typing import Sequence
import re

logger = logging .getLogger(__name__)


def bib2rest(input_bibfile, output_txtfile):
    """ Converts citation formats from bibtex to rst

    Last commit to https://github.com/cykustcc/bib2reSTcitation was 5 years ago and there's no
    installable package on pypi so for convenience we duplicate the package here (it's MIT licensed, see LICENSE)

    # Original Author Yukun Chen cykustc@gmail.com
    """
    start_pattern = re.compile(r"^(?: |\t)*\@(?:book|article|incollection|inproceedings)\{([a-z0-9]+), *$")
    title_pattern = re.compile(r"^(?: |\t)*title=\{([a-zA-Z0-9 ]+)\}(?: |\t)*,(?: |\t)*$")
    author_pattern = re.compile(r"^(?: |\t)*author=\{([a-zA-Z0-9 ,;\.\-]+)\}(?: |\t)*,(?: |\t)*$")
    other_info_pattern = re.compile(r"^(?: |\t)*(?:journal|volume|number|year|publisher|pages|organization|booktitle)=\{([a-zA-Z0-9 ,;\.-]+)\}(?: |\t)*,(?: |\t)*$")
    end_pattern = re.compile("^(?: |\t)*}(?: |\t)*$")
    with open(input_bibfile, 'r') as input_handle:
        with open(output_txtfile, 'w') as output_handle:
            in_a_bib_block = False
            rest_ref_block = ""
            title = ""
            author = ""
            ref = ""
            output_handle.write(".. _references:\n\n==========\nReferences\n==========\n\n")
            for line in input_handle:
                if not in_a_bib_block:
                    # not in a bib block
                    if start_pattern.match(line):
                        matches = start_pattern.match(line)
                        in_a_bib_block = True
                        ref = matches.group(1)
                    else:
                        pass

                else:
                    # in a bib block
                    if end_pattern.match(line):
                        matches = end_pattern.match(line)
                        in_a_bib_block = False
                        rest_ref_block = ".. [" + ref + "]" + " " + author + ", " + title + ", " + other_info
                        output_handle.write(rest_ref_block + "\n\n")
                    elif title_pattern.match(line):
                        matches = title_pattern.match(line)
                        title = matches.group(1)
                    elif author_pattern.match(line):
                        matches = author_pattern.match(line)
                        author = matches.group(1)
                    elif other_info_pattern.match(line):
                        matches = other_info_pattern.match(line)
                        other_info = matches.group(1)
                        rest_ref_block = rest_ref_block + ", " + other_info
                    else:
                        pass


def requires_conversion(filenames: Sequence[str], bib_file: str) -> bool:
    """ Uses filenames list to check if the bibliography file has changed
    """
    return True
    print('filenames:', filenames)
    print('bibfile:', bib_file)
    if bib_file in filenames:
        print('BIB IN FILES')
        return True
    return False


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed',
    )
    parser.add_argument(
        '--bib-file', type=str, default='docs/source/bibliography.bib',
        help='The bibtex bibliography file to convert',
    )
    parser.add_argument(
        '--rst-file', type=str, default='docs/source/bibliography.rst',
        help='THe output rst file that will contain the reST formatted citations',
    )

    args = parser.parse_args(argv)
    if requires_conversion(args.filenames, args.bib_file):
        try:
            bib2rest(args.bib_file, args.rst_file)
        except Exception as e:
            logger.exception(e)
            return 1
        return 0
    return 0


if __name__ == '__main__':
    exit(main())
