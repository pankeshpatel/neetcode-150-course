# Two Integer Sum II
# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given
# target number target and index1 < index2. Note that index1 and index2 cannot be equal,
# therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use
# O(1)
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

# numbers = [2, 3, 4]
# target = 6


# Approach - 1

# time complextiy using Array : O(nlogn) + O(n)


# numbers = [1, 2, 3, 4]
# target = 7

# numbers.sort()  # O(nlogn)


# index_1 = 0
# index_2 = len(numbers) - 1

# while index_1 < index_2:  # O(n)
#     currentSum = numbers[index_1] + numbers[index_2]

#     if currentSum > target:
#         index_2 -= 1
#     elif currentSum < target:
#         index_1 += 1
#     else:
#         print(f"{index_1}...{index_2}")
#         break


### Approach 2 - Hash Map


numbers = [1, 2, 3, 4]
target = 7


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#         hashmap: dict[int, int] = {}
#         index_1 = -1
#         index_2 = -1

#         # for index in range(len(nums)):  # O(n)
#         #     remaining_element = target - nums[index]
#         #     number = nums[index]
#         #     if remaining_element in hashmap:
#         #         index_1 = hashmap[remaining_element]
#         #         index_2 = index
#         #     else:
#         #         hashmap[number] = index

#         # return [index_1, index_2]

#         for index, number in enumerate(nums):
#             remaining_element = target - number
#             if remaining_element in hashmap:
#                 index_1 = hashmap[remaining_element]
#                 index_2 = index
#             else:
#                 hashmap[number] = index

#         return [index_1, index_2]

from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:

    index_map = {}

    for index, num in enumerate(nums):
        value = target - num
        if value in index_map:
            return [index, index_map[value]]
        index_map[num] = index

    return []
