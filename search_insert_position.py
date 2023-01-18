# search insert position

def searchInsert(nums, target) -> int:
    start = 0
    end = len(nums) - 1

    if target > nums[-1]:
        return end + 1
    elif target < nums[0]:
        return 0
    print(f"\ntarget: {target}, end: {end}")
    return binary_search(nums, target, start, end)


def binary_search(nums, target, start, end):
    current_range = end - start

    midpoint_index = start + (end - start) // 2
    midpoint = nums[midpoint_index]

    print(nums[start:end + 1], midpoint)
    if current_range <= 2:
        if target == nums[start]:
            return start
        elif target == nums[end]:
            return end
        else:
            return start + 1

    if midpoint == target:
        return midpoint_index
    elif midpoint > target:
        return binary_search(nums, target, start, midpoint_index + 1)
    elif midpoint < target:
        return binary_search(nums, target, midpoint_index, end)


# def searchInsert(nums, target):
#     max_index = len(nums)
#     midpoint_index = max_index //2
#     midpoint_value = nums[midpoint_index]
#
#     if target > nums[-1]:
#         return max_index
#     elif target < nums[0]:
#         return 0
#     elif max_index == 2 and target not in nums:
#         return 1
#
#
#     if midpoint_value == target:
#         return midpoint_index
#     elif midpoint_value > target:
#         return searchInsert(nums[0:midpoint_index], target)
#     elif midpoint_value < target:
#         return midpoint_index + searchInsert(nums[midpoint_index:-1], target) + 1
#
# # [....................]
#           [..........]
#                 []
# print(searchInsert([1,3,5,6], 5))
# print(searchInsert([1,3,5,6], 2))
# print(searchInsert([1], 1))
# print(searchInsert([1,3,5,6,9,10,11], 8))
# print(searchInsert([1,3,5,6,9,10], 8))
print(searchInsert([1, 3, 5, 6], 7))
# print(searchInsert([1,3,5,6], -4))
# print(searchInsert([1, 3], 1))
# print(searchInsert([1, 3], 2))
# print(searchInsert([1, 3], 3))
print(searchInsert([1, 3, 5], 4))

# searchInsert([1,3,5,6], 2)            == (2) + 1
#     searchInsert([1,3,5], 2)          == (1) +
#         searchInsert([1,3], 2)        == 1
#
# searchInsert([1,3,5,7], 6)            == (2) + 1
#     searchInsert([3,5, 7], 6)         1 + 1
#         searchInsert([5,7], 6)          1
