import pytest

from puzzle import Grid


@pytest.fixture(scope="function")
def grid():
    return Grid([["a", "b", "c"], ["m", "o", "y"]], length=3, depth=2)


def test_grid_instance(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    assert grid.length == 3
    assert grid.depth == 2
    assert grid.grid == [["a", "b", "c"], ["m", "o", "y"]]
    assert grid._letters is None
    assert grid._number == 0


def test_grid_to_string(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    assert str(grid) == "a | b | c\nm | o | y"


def test_grid_as_table(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    assert grid.as_table() == "a | b | c\nm | o | y"


def test_grid_get_item(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    assert grid[0] == ["a", "b", "c"]
    assert grid[-1] == ["m", "o", "y"]


def test_grid_get_item_out_of_scope(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    with pytest.raises(IndexError):
        assert not grid[2]


def test_grid_length(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    assert len(grid) == 2


def test_grid_iteration(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    for row in grid:
        assert isinstance(row, list)
        assert any(isinstance(letter, str) for letter in row)


def test_grid_max_size(grid):
    assert grid.max_size == 3


def test_grid_letters(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    exp_letters = {"a", "b", "c", "m", "o", "y"}
    assert grid._letters is None
    assert grid.letters == exp_letters
    assert grid._letters == exp_letters


def test_grid_horizontal_lines(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    assert grid.horizontal_lines == ["abc", "cba", "moy", "yom"]


def test_grid_vertical_lines(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    assert grid.vertical_lines == ["am", "ma", "bo", "ob", "cy", "yc"]


def test_grid_diagonal_lines(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    exp_words = ("ao", "oa", "a", "by", "yb", "bm", "mb", "c", "co", "oc")
    result = grid.diagonal_lines
    assert len(result) == len(exp_words)
    for exp_word in exp_words:
        assert exp_word in result


def test_grid_lines(grid):
    """
    Grid:
    [
        ["a", "b", "c"],
        ["m", "o", "y"]
    ]
    """
    exp_lines = [
        'am', 'ma', 'bo', 'ob', 'cy', 'yc',
        'abc', 'cba', 'moy', 'yom',
        "ao", "oa", "by", "yb", "c",
        "a", "bm", "mb", "co", "oc"
    ]
    assert grid._lines is None
    result = grid.lines
    assert grid._lines == result
    assert len(result) == len(exp_lines)
    for exp_line in exp_lines:
        assert exp_line in result
