import pytest
from employee_that_worked_on_the_longest_task import hardest_worker


def test_example_1():
    n = 10
    logs = [[0, 3], [2, 5], [0, 9], [1, 15]]
    assert hardest_worker(n, logs) == 1


def test_example_2():
    n = 26
    logs = [[1, 1], [3, 7], [2, 12], [7, 17]]
    assert hardest_worker(n, logs) == 3


def test_example32():
    n = 2
    logs = [[0, 10], [1, 20]]
    assert hardest_worker(n, logs) == 0
