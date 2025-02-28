# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:

# Input: nums = [0,1,1]

# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]

# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# sort the array

# [-1, 0, 1, 2, -1, -4]

# [-4, -1, -1, 0, 1, 2]

# i, j, k

# i = 0
# j = i + 1
# k = len(nums) - 1


# while i < k:
#     currentSum = nums[i] + nums[j] + nums[k]

#     if currentSum < 0:
#         i = i + 1
#         j = i + 1

#     elif currentSum > 0:
#         k = k - 1
#     else:
#         return [nums[i], nums[j], nums[k]]

# return []


# i = 0
# j = len(num) - 1

nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
res = []

for i, a in enumerate(nums):
    l = i + 1
    r = len(nums) - 1
    while l < r:
        threeSum = a + nums[l] + nums[r]

        if threeSum > 0:
            r -= 1
        elif threeSum < 0:
            l += 1
        else:
            res.append([a, nums[l], nums[r]])
            l += 1
            r -= 1
            while nums[l] == nums[l - 1] and l < r:
                l += 1

print(f"{res}")
