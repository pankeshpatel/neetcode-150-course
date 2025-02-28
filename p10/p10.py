# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.

# s = "Was it a car or a cat I saw?"
s = "tab a cat"
# s = "Madam, in Eden, I'm Adam"

import re

# s = "Was it a car or a cat I saw?"
cleaned_s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
print(cleaned_s)
palidromFlag = False

if len(cleaned_s) == 0:
    palidromFlag = True

front_p = 0
back_p = len(cleaned_s) - 1


while front_p <= back_p:
    if cleaned_s[front_p] == cleaned_s[back_p]:
        palidromFlag = True
        front_p += 1
        back_p -= 1
    else:
        palidromFlag = False
        break


print(f"{palidromFlag}")
