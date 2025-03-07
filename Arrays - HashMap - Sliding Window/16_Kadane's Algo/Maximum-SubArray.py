# Maximum Subarray
# Given an array of integers nums, find the subarray with the largest sum and return the sum.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [2,-3,4,-2,2,1,-1,4]

# Output: 8
# Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

# Example 2:

# Input: nums = [-1]

# Output: -1


nums = [2, -3, 4, -2, 2, 1, -1, 4]
currentSum = 0
maxSum = 0

for n in nums:
    if currentSum < 0:
        currentSum = 0
    currentSum += n
    maxSum = max(currentSum, maxSum)

print(f"{maxSum}")
