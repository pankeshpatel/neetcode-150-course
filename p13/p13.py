# Container With Most Water
# You are given an integer array heights where heights[i] represents the height of the
# ith bar.

# You may choose any two bars to form a container.
# Return the maximum amount of water a container can store.

# example 1
# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36

# example 2

# Input: height = [2,2,2]

# Output: 4

height = [1, 7, 2, 5, 4, 7, 3, 6]

l = 0
r = len(height) - 1
result = 0

while l < r:

    area = min(height[l], height[r]) * r - l
    result = max(result, area)

    if height[l] <= height[r]:
        l += 1
    else:
        r -= 1


print(f"{result}")
