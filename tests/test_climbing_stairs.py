import pytest
from climbing_stairs import climb_stairs


def test_example_2():
    n = 2
    assert climb_stairs(n) == 2


def test_example_3():
    n = 3
    assert climb_stairs(n) == 3


def test_example_4():
    n = 4
    assert climb_stairs(n) == 5


def test_big_number():
    n = 45
    print(climb_stairs(n))
