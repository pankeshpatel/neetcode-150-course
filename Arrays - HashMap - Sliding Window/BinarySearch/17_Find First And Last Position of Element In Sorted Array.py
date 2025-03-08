# Find First and Last Position of Element in Sorted Array
# Medium
# Topics
# Companies
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

nums = [5, 7, 7, 8, 8, 10]
target = 8


def binarySearch(nums, target, leftBias):
    l = 0
    r = len(nums) - 1
    i = -1

    while l <= r:
        m = int((r + l) // 2)
        # print(f"{l}..{r}..{m}")
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            i = m
            if leftBias:
                r = m - 1
            else:
                l = m + 1
    return i


left = binarySearch(nums, target, True)
right = binarySearch(nums, target, False)

print(f"{left}..{right}")
