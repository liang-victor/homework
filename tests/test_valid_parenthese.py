from valid_parentheses import is_valid


def test_example_1():
    s = '()'
    assert is_valid(s) == True


def test_multiple_adjacent_brackets():
    s = "()[]{}"
    assert is_valid(s) == True


def test_mismatched_brackets():
    s = "(]"
    assert is_valid(s) == False


def test_nested_brackets():
    s = "([])"
    assert is_valid(s) == True


def test_nested_mismatch():
    s = "([)]"
    assert is_valid(s) == False


def test_unbalanced_open():
    s = '('
    assert is_valid(s) == False


def test_unbalanced_close():
    s = ')'
    assert is_valid(s) == False
