from argparse import ArgumentTypeError
from pathlib import Path

import pytest

from puzzle.cli import positive_int, parser


@pytest.mark.parametrize("number", ("12", "666"))
def test_positive_int(number):
    assert positive_int(number) == int(number)


@pytest.mark.parametrize("number", ("abc", "0", "-12"))
def test_positive_int_with_invalid_numbers(number):
    with pytest.raises(ArgumentTypeError):
        assert positive_int(number)


def test_parser_with_default_params():
    args = parser([])
    assert args.file == Path("puzzle/words.txt").resolve()
    assert args.length == 15
    assert args.depth == 15
    assert args.quiet is False


def test_parser_with_custom_params():
    args = parser(
        ["--length", "12", "--depth", "5", "--file", "my.txt", "--quiet"]
    )
    assert args.file == Path("my.txt")
    assert args.length == 12
    assert args.depth == 5
    assert args.quiet is True
