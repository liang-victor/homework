"""242. Valid Anagram

https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


def is_anagram(s: str, t: str) -> bool:
    character_counts = {}
    for char in s:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    for char in t:
        if char not in character_counts or character_counts[char] == 0:
            return False
        else:
            character_counts[char] -= 1
    return all(remaining_count == 0 for remaining_count in character_counts.values())
