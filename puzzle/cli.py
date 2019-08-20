import sys

from argparse import ArgumentParser

from puzzle import Finder, GridMaker


def parser():
    menu = ArgumentParser(
        "Puzzle",
        description="Programme generate crossword puzzle and "
                    "try to find exist words from file"
    )
    menu.add_argument(
        "-f", "--file",
        dest="file",
        type=str,
        default="words.txt",
        help="you can to change file with words",
    )
    menu.add_argument(
        "-l", "--length",
        dest="length",
        type=int,
        default=15,
        help="you can to choice board length",
    )
    menu.add_argument(
        "-d", "--depth",
        dest="depth",
        type=int,
        default=15,
        help="you can to choice board depth",
    )
    menu.add_argument(
        "-q", "--quiet",
        dest="quiet",
        action="store_true",
        help="you can to disable verbose mode",
    )
    return menu.parse_args()


def main():
    params = parser()
    grid = GridMaker(length=params.length, depth=params.depth).generate()
    if not params.quiet:
        print(f"Was generated puzzle size of {grid.length}x{grid.depth}:")
        print(grid)

    finder = Finder(grid)
    words = finder.find_words(params.file)
    print(f"Found {len(words)} words:")
    if not params.quiet:
        print(words)
