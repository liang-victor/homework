from longest_substring_without_repeating_characters import length_of_longest_substring


def test_example_1():
    s = "abcabcbb"
    result = length_of_longest_substring(s)
    assert result == 3


def test_example_2():
    s = "bbbbb"
    result = length_of_longest_substring(s)
    assert result == 1


def test_example_3():
    s = "pwwkew"
    result = length_of_longest_substring(s)
    assert result == 3


def test_empty_string():
    s = ""
    result = length_of_longest_substring(s)
    assert result == 0


def test_space_string():
    s = " "
    result = length_of_longest_substring(s)
    assert result == 1


def test_dvdf():
    s = "dvdf"
    result = length_of_longest_substring(s)
    assert result == 3


def test_cross_a_double_character():
    s = "abcdefggh"
    result = length_of_longest_substring(s)
    assert result == 7


def test_abba():
    s = "abba"
    result = length_of_longest_substring(s)
    assert result == 2


def test_tmmzuxt():
    s = "tmmzuxt"
    result = length_of_longest_substring(s)
    assert result == 5
