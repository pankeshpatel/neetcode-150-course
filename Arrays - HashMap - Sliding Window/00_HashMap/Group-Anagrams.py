# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists.
# You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but
# the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.


def construct_hashMap(str_element):
    charMap = {chr(i): 0 for i in range(ord("a"), ord("z"))}

    for index in range(len(str_element)):
        str_char = str_element[index]
        charMap[str_char] += 1

    return tuple(charMap.values())


strs = ["act", "pots", "tops", "cat", "stop", "hat"]


# if len(strs) == 0:
#     return []


# initialize a hash-map with all zero
strMap = {}


for str_element in strs:
    key = construct_hashMap(str_element)
    print(f"{key}...{str_element}")

    # check key if exists
    if key in strMap:
        # if key exists then append value to the existing list.
        strMap[key].append(str_element)
    else:
        strMap[key] = [str_element]
        # if key does not exits then add the key and add value into a list

print(list(strMap.values()))
