"""Remove Duplicates from Sorted Array

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

- integer array nums is in non-decreasing order
- remove the duplicates in-place
    - if there are k unique elements, then the first k values should hold the final result
"""


def remove_duplicates(nums):
    pointer = 0
    last_value = None

    for i, value in enumerate(nums):
        if value != last_value:
            nums[pointer] = value
            pointer += 1
        last_value = value
    return pointer
