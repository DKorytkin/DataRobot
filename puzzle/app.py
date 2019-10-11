import itertools
import random

from pathlib import Path
from string import ascii_lowercase
from typing import List, Set, Iterator, Iterable


GRID_TYPE = List[List[str]]


def read_words(path: Path) -> Iterator:
    """
    Lazy read words from file
    :param Path path: fro example ./words.txt
    :return: words iterator
    """
    if not (path.exists() and path.is_file()):
        raise FileNotFoundError(f"Please, check your path to file {path}")

    with open(path, "r") as f:
        for line in f.readlines():
            yield line.strip()


def filter_by_letters(
    words: Iterator[str], letters: Iterable[str]
) -> Iterator:
    """
    Filtered words by the first letter if that exist into the grid
    >>> list(filter_by_letters(["by", "world", "test"], ["b", "w"]))
    ["by", "world"]
    >>> list(filter_by_letters(["by", "world", "test"], ["b", "w", "t"]))
    ["by", "world", "test"]

    :param Iterator[str] words: ["by", "world", "test"]
    :param Iterable[str] letters: ["b", "w"]
    :return: filtered words iterator ["by", "world"]
    """
    for word in words:
        first_letter = word[0]
        if first_letter in letters:
            yield word


def filter_by_length(words: Iterator, length: int) -> Iterator:
    """
    Filtered words by length if that length not more of grid size
    >>> list(filter_by_length(["by", "world"], 3))
    ["by"]
    >>> list(filter_by_length(["by", "world"], 4))
    ["by", "world"]

    :param Iterator[str] words: ["by", "world"]
    :param int length: 3
    :return: filtered words iterator ["by"]
    """
    for word in words:
        if len(word) <= length:
            yield word


class Grid:
    def __init__(self, grid: GRID_TYPE, length: int, depth: int):
        self.grid = grid
        self.length = length
        self.depth = depth
        self._letters = None
        self._lines = None
        self._number = 0

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.as_table()

    def __getitem__(self, item):
        return self.grid[item]

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.grid)

    def __next__(self):
        if self._number >= len(self.grid):
            self._number = 0
            raise StopIteration

        result = self.grid[self._number]
        self._number += 1
        return result

    def as_table(self) -> str:
        """
        Make simple table of grid
        """
        return "\n".join([" | ".join(row) for row in self.grid])

    @property
    def max_size(self) -> int:
        return max(self.length, self.depth)

    @property
    def letters(self) -> Set[str]:
        """
        Get all letters of grid
        >>> self.grid
        [
            ['u', 'f', 'h'],
            ['o', 'q', 'i'],
        ]
        >>> self.letters
        {'u', 'f', 'h', 'o', 'q', 'i'}
        :return: set letters of grid
        """
        if not self._letters:
            self._letters = {l for l in itertools.chain(*self.grid)}
        return self._letters

    def all_lines(self) -> List[str]:
        """
        Get all diagonal lines of grid
        also revert line included
        >>> self.grid
        [
            ["a", "b", "c"],
            ["m", "o", "y"]
        ]
        >>> self.all_lines
        {
            "abc", "cba", "moy", "yom",
            "am", "ma", "bo", "ob", "cy", "yc",
            "ao", "oa", "a", "by", "yb", "bm", "mb", "c", "co", "oc",
        }
        """
        words = set()
        for length_index in range(0, self.length):
            vertical_letters = []
            left_letters, right_letters = [], []
            for depth_index in range(0, self.depth):
                if length_index == 0:
                    horizontal_letters = "".join(self.grid[depth_index])
                    words.add(horizontal_letters)
                    words.add(horizontal_letters[::-1])

                vertical_letters.append(self.grid[depth_index][length_index])

                right_index = length_index + depth_index
                if depth_index == 0:
                    left_letters.append(self.grid[depth_index][right_index])
                    right_letters.append(self.grid[depth_index][right_index])
                    continue

                if right_index < self.length:
                    right_letters.append(self.grid[depth_index][right_index])

                left_index = length_index - depth_index
                if self.length > left_index >= 0:
                    left_letters.append(self.grid[depth_index][left_index])

            right_letters = "".join(right_letters)
            if right_letters:
                words.add(right_letters)
                words.add(right_letters[::-1])

            left_letters = "".join(left_letters)
            if left_letters:
                words.add(left_letters)
                words.add(left_letters[::-1])

            vertical_letters = "".join(vertical_letters)
            words.add(vertical_letters)
            words.add(vertical_letters[::-1])
        return list(words)

    @property
    def lines(self) -> List[str]:
        """
        Get all possible lines of grid
        - vertical
        - horizontal
        - diagonal
        """
        if not self._lines:
            self._lines = self.all_lines()
        return self._lines


class GridMaker:
    def __init__(self, length: int, depth: int):
        self.length = length
        self.depth = depth

    def __str__(self):
        return f"<GridMaker length={self.length} depth={self.depth}>"

    def _random_row(self) -> List[str]:
        """
        Generate row with random letters
        """
        return [random.choice(ascii_lowercase) for _ in range(self.length)]

    def generate(self) -> Grid:
        """
        Generate puzzle of random letters
        How to use:
        >>> gm = GridMaker(length=3, depth=2)
        >>> gm.generate()
        [
            ['u', 'u', 'h'],
            ['o', 'q', 'i'],
        ]
        :return: puzzle
        """
        result = [self._random_row() for _ in range(self.depth)]
        return Grid(result, length=self.length, depth=self.depth)


class Finder:
    def __init__(self, grid: Grid):
        self.grid = grid

    def find_words(self, file_path: str) -> List[str]:
        """
        Method try to find all words from the file into the grid
        :param file_path: for example ./words.txt
        :return: found words
        """
        exist_words = []
        all_possible_lines = "|".join(self.grid.lines)
        words = read_words(file_path)
        words = filter_by_length(words, self.grid.max_size)
        words = filter_by_letters(words, self.grid.letters)
        for word in words:
            if word in all_possible_lines:
                exist_words.append(word)
        return exist_words
