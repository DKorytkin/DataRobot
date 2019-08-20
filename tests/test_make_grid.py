from string import ascii_lowercase

from puzzle import GridMaker, Grid


def test_grid_maker_instance():
    size = 15
    gm = GridMaker(length=size, depth=size)
    assert gm.length == size
    assert gm.depth == size


def test_grid_maker_to_string():
    length, depth = 2, 3
    gm = GridMaker(length=length, depth=depth)
    assert str(gm) == "<GridMaker length=2 depth=3>"


def test_grid_maker_random_row():
    length, depth = 2, 3
    gm = GridMaker(length=length, depth=depth)
    row = gm._random_row()
    assert len(row) == length
    assert all([isinstance(w, str) and w in ascii_lowercase for w in row])


def test_grid_maker_generate():
    length, depth = 12, 5
    gm = GridMaker(length=length, depth=depth)
    grid = gm.generate()
    assert isinstance(grid, Grid)
    assert len(grid) == depth
    for row in grid:
        assert len(row) == length
        assert all([isinstance(w, str) and w in ascii_lowercase for w in row])
