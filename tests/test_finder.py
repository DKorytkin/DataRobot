import os
from pathlib import Path
from typing import Iterator

import pytest

from puzzle.app import (
    Grid,
    Finder,
    filter_by_letters,
    filter_by_length,
    read_words,
)


GRID = [["a", "b", "c"], ["y", "n", "i"]]
WORDS = ["ci", "by", "an", "test", "and", "apple", "in", "abc"]


@pytest.fixture(scope="module")
def file_path() -> Path:
    f_path = Path("secret_file_path.txt")
    with open(f_path, "+w") as f:
        f.write("\n".join(WORDS))
    yield f_path
    os.remove(f_path)


@pytest.fixture()
def finder() -> Finder:
    return Finder(grid=Grid(grid=GRID, length=3, depth=2))


def test_finder_instance(finder):
    assert isinstance(finder.grid, Grid)
    assert finder.grid.grid == GRID


def test_read_words(file_path):
    words = read_words(file_path)
    assert isinstance(words, Iterator)
    assert list(words) == WORDS


def test_read_words_with_invalid_path():
    with pytest.raises(FileNotFoundError):
        assert list(read_words(Path("test_read_words_with_invalid_path.txt")))


def test_filter_by_letters():
    words = filter_by_letters(WORDS, ["a", "c"])
    assert isinstance(words, Iterator)
    assert list(words) == ["ci", "an", "and", "apple", "abc"]


def test_filter_by_length():
    words = filter_by_length(WORDS, 2)
    assert isinstance(words, Iterator)
    assert list(words) == ["ci", "by", "an", "in"]


def test_find_words(finder, file_path):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["y", "n", "i"]
    ]
    """
    assert finder.find_words(file_path) == ["ci", "by", "an", "in", "abc"]
