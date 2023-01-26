import pytest
from ransom_note import can_construct


def test_example_1():
    ransomNote = "a"
    magazine = "b"

    assert can_construct(ransomNote, magazine) is False


def test_example_2():
    ransomNote = "aa"
    magazine = "ab"

    assert can_construct(ransomNote, magazine) is False


def test_example_3():
    ransomNote = "aa"
    magazine = "aab"

    assert can_construct(ransomNote, magazine) is True
