"""https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest
substring without repeating characters."""


def length_of_longest_substring(s: str) -> int:
    """Given a string s, find the length of the longest substring without repeating characters.

    We can traverse the string, and keep track of where we last saw each character's position in a dictionary
    When a character is already present in the dict, calculate the number of characters since we last saw it
    and compare it to the maximum value we have seen so far
    """

    chars = set()
    longest_substring = 0
    left = 0
    for right in range(len(s)):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[right])
        longest_substring = max(longest_substring, right - left + 1)

    return longest_substring
