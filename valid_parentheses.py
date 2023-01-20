"""https://leetcode.com/problems/valid-parentheses/

"""


def is_valid(s):
    brackets = {')': '(', '}': '{', ']': '['}
    open_brackets = set(brackets.values())

    stack = []

    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif not stack or brackets[char] != stack.pop():
            return False
    return len(stack) == 0
