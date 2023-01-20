"""Maximum Subarray

https://leetcode.com/problems/maximum-subarray/description/
"""


def max_subarray(nums):
    """Given an integer array nums, find the subarray with the largest sum, and return its sum.

    If we take the cumulative sum of values across the array, it can be observed that:
        - if the cumulative sum stays above zero, it's worth including in a subarray
        - if the cumulative sum goes below zero, the better option would be to start a new subarray at the
        next positive integer

     With this in mind, we can take the cumulative sum across the array while resetting as needed, and keep track
     of the highest cumulative sum seen to get the maximum subarray sum.
    """

    cumulative_sum = 0
    max_value = nums[0]

    for value in nums:
        if cumulative_sum < 0:
            cumulative_sum = value
        else:
            cumulative_sum += value

        if cumulative_sum > max_value:
            max_value = cumulative_sum
    return max_value
