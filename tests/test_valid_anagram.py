import pytest
from valid_anagram import is_anagram


def test_example_1():
    s = "anagram"
    t = "nagaram"
    assert is_anagram(s, t) is True


def test_example_2():
    s = "rat"
    t = "car"
    assert is_anagram(s, t) is False


def test_example_3():
    s = "ab"
    t = "a"
    assert is_anagram(s, t) is False
