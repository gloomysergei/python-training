from solution import triangle


def test_triangle():
    assert triangle(0) == [1]
    assert triangle(1) == [1, 1]
    assert triangle(2) == [1, 2, 1]
    assert triangle(3) == [1, 3, 3, 1]
    assert triangle(4) == [1, 4, 6, 4, 1]
    assert triangle(8) == [1, 8, 28, 56, 70, 56, 28, 8, 1]