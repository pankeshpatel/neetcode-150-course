# Two Integer Sum II


# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use
# O
# (
# 1
# )
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sorted_nums = sorted(numbers)

        index_1 = 0
        index_2 = len(sorted_nums) - 1

        while index_1 < index_2:
            currentSum = sorted_nums[index_1] + sorted_nums[index_2]

            if currentSum > target:
                index_2 -= 1
            elif currentSum < target:
                index_1 += 1
            else:
                return [index_1 + 1, index_2 + 1]

        return []
