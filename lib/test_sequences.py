from lib.sequences import print_fibonacci


def test_fibonacci():
    assert print_fibonacci(0) == []
    assert print_fibonacci(1) == [0]
    assert print_fibonacci(2) == [0, 1]
    assert print_fibonacci(5) == [0, 1, 1, 2, 3]
    assert print_fibonacci(9) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
