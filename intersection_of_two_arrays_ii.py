"""Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear
as many times as it shows in both arrays and you may return the result in any order.


"""


def intersect(nums1, nums2):
    nums_1_counts = count_values(nums1)

    intersection = []
    for n in nums2:
        if n in nums_1_counts and nums_1_counts[n] > 0:
            intersection.append(n)
            nums_1_counts[n] -= 1
    return intersection


def count_values(nums):
    counts = {}
    for value in nums:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts
