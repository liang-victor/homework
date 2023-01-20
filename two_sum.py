"""1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(nums, target):
    """Returns indices of two numbers in the array that add up to target

    Uses a dictionary to look up previously seen values
    """
    nums_dict = {}

    for current_index, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [nums_dict[complement], current_index]
        nums_dict[num] = current_index
