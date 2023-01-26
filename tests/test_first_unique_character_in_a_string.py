import pytest
from first_unique_character_in_a_string import first_unique_char


def test_example_1():
    s = "leetcode"
    assert first_unique_char(s) == 0


def test_example_2():
    s = "loveleetcode"
    assert first_unique_char(s) == 2


def test_example_3():
    s = "aabb"
    assert first_unique_char(s) == -1
