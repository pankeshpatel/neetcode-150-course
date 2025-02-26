# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is
# the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in
# O(n)
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]


# Approach # 1
nums = [-1, 0, 1, 2, 3]

# approach # 1 - brute force
# output = []
# for i in range(len(nums)):
#     mul = 1
#     for j in range(len(nums)):
#         if i != j:
#             mul = mul * nums[j]
#     output.append(mul)

# print(output)

# approach # 2
n = len(nums)
result = [0] * n
prefix = [0] * n
postfix = [0] * n

prefix[0] = postfix[n - 1] = 1

for i in range(1, n):
    prefix[i] = nums[i - 1] * prefix[i - 1]

for i in range(n - 2, -1, -1):
    postfix[i] = postfix[i + 1] * nums[i + 1]

for i in range(n):
    result[i] = prefix[i] * postfix[i]

print(result)
