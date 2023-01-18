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

@pytest.mark.fail_slow(1)
def test_big_number():
    n = 35
    climb_stairs(n)
