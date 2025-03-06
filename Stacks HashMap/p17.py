# Valid Parentheses
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.


class Solution:

    def isValid(self, s: str) -> bool:
        StringHashMap = {"}": "{", "]": "[", ")": "("}
        stack = []

        for i in range(0, len(s)):
            if s[i] in StringHashMap:
                if stack and stack[-1] == StringHashMap[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        return True if not stack else False


my_string = Solution()
s = "([{}])"
print(my_string.isValid(s))
