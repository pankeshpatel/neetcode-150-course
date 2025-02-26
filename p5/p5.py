# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]

# nums = [7, 7]


nums = [1, 2, 2, 2, 3, 3, 4, 6]
k = 2

num_map = {}

for i in range(len(nums)):
    n = nums[i]
    if n in num_map:
        num_map[n] += 1
    else:
        num_map[n] = 1

# sorting by value
sorted_by_values_desc = dict(
    sorted(num_map.items(), key=lambda item: item[1], reverse=True)
)

print(list(sorted_by_values_desc.keys())[:k])
