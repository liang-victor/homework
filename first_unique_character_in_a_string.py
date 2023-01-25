"""387. First Unique Character in a String

https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


def first_unique_char(s: str) -> int:
    character_count = {}
    for char in s:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    for i, char in enumerate(s):
        if character_count[char] == 1:
            return i

    return -1
