# Given an array of integers nums and an integer target, return the indices
# i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input:
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]


# Constraints:
# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000

# Approach # 1

# nums = [3, 4, 5, 6]
# target = 7
# index_1 = -1
# index_2 = -1


# for index in range(len(nums)):
#     remaining_element = target - nums[index]
#     if remaining_element in nums[index + 1 :]:
#         print("elements exists")
#         index_1 = index
#         index_2 = nums.index(remaining_element, index + 1)
#         break

# print(f"{index_1}...{index_2}")


## Approach # 2 - use hashmap to reduce a search


hashmap: dict[int, int] = {}
nums = [4, 5, 6]
target = 10
index_1 = -1
index_2 = -1


for index in range(len(nums)):
    remaining_element = target - nums[index]

    if remaining_element in hashmap:
        index_1 = index
        index_2 = hashmap[remaining_element]
    else:
        number = nums[index]
        hashmap[number] = index


print(f"{index_1}...{index_2}")
