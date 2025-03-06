# Binary Search
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in
# O(logn) time.

# Example 1:

# Input: nums = [-1,0,2,4,6,8], target = 4

# Output: 3
# Example 2:

# Input: nums = [-1,0,2,4,6,8], target = 3

# Output: -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
resultIndex = -1


l, r = 0, len(nums) - 1

while l <= r:
    m = l + ((r - l) // 2)
    if nums[m] > target:
        r = m - 1
    elif nums[m] < target:
        l = m + 1
    else:
        resultIndex = m


print(f"{resultIndex}")
