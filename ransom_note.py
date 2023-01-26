"""383. Ransom Note

https://leetcode.com/problems/ransom-note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



"""


def can_construct(ransomNote: str, magazine: str) -> bool:
    """Check if ransomNote is a subset/anagram of magazine
    """

    character_count = {}
    for char in magazine:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    for char in ransomNote:
        if char not in character_count or character_count[char] == 0:
            return False
        else:
            character_count[char] -= 1
    return True
