# Permutation in String
# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise.
# That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:

# Input: s1 = "abc", s2 = "lecaabee"

# Output: false

# Resource:  Permutation in String
# https://www.youtube.com/watch?v=VXewy91P0S4

s1 = "ab"
s2 = "lecabee"


def createHashMap(input_string):
    hashMapString = {}
    for s in input_string:
        if s in hashMapString:
            hashMapString[s] += 1
        else:
            hashMapString[s] = 1

    return hashMapString


hashMapSubString = createHashMap(s1)

l = 0
r = len(s1)
subStringFlag = False


while r <= len(s2):
    substring = createHashMap(s2[l:r])
    if substring == hashMapSubString:
        subStringFlag = True
        break
    else:
        l = l + 1
    r = r + 1

print(f"{subStringFlag}")
