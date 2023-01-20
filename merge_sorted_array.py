"""https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
 and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""


def merge(nums1, m, nums2, n):
    """Two sorted arrays (of length m and n) will be sorted into a single sorted array


    Modifies nums_1 inplace
    """
    if n == 0:
        return nums1

    result = []

    i = 0

    for num_1 in nums1[:m]:
        while i < n and nums2[i] <= num_1:
            result.append(nums2[i])
            i += 1
        result.append(num_1)

    # append any leftovers
    while i < n:
        result.append(nums2[i])
        i += 1

    for i, _ in enumerate(nums1):
        nums1[i] = result[i]
