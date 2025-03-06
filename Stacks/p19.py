# Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Example 1:

# Input: tokens = ["1","2","+","3","*","4","-"]

# Output: 5

# Explanation: ((1 + 2) * 3) - 4 = 5


class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                sum = int(stack.pop()) + int(stack.pop())
                stack.append(sum)
            elif c == "-":
                a, b = int(stack.pop()), int(stack.pop())
                sub = b - a
                stack.append(sub)
            elif c == "*":
                mul = int(stack.pop()) * int(stack.pop())
                stack.append(mul)
            elif c == "/":
                a, b = int(stack.pop()), int(stack.pop())
                div = int(b / a)
                stack.append(div)
            else:
                stack.append(c)

        return stack[0]


tokenObj = Solution()
token = ["1", "2", "+", "3", "*", "4", "-"]
print(tokenObj.evalRPN(token))
