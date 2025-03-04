# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1

input_string = "au"
length = 0
strMap = set()
l = 0

# if len(input_string) == 0:
#     length = 0

for r in range(0, len(input_string)):
    while input_string[r] in strMap:
        strMap.remove(input_string[l])
        l = l + 1

    strMap.add(input_string[r])
    length = max(length, r - l + 1)

print(f"{strMap}...{length}")
