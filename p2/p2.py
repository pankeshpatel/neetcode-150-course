# Leetcode 242 - Valid Anagram

# Given two strings s and t, return true if t is an anagram of s and false otherwise.

# anagram means - every single characters present in s, it should be present in t

# s: cat ; t: tac ; True
# s: ram ; t: rat;  False

s = "ram"
t = "ratp"

result = False

if len(s) != len(t):
    result = False
else:
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    print(f"{sorted_s}...{sorted_t}")

    for index in range(len(s)):
        if sorted_s[index] == sorted_t[index]:
            result = True
        else:
            result = False
            break

print(f"the result is {result}")
