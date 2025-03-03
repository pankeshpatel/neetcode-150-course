# Best Time to Buy and Sell Stock
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:

# Input: prices = [10,8,7,5,2]

# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.


prices = [10, 1, 5, 6, 7, 1]

l, r = 0, 1
maxP = 0

while r < len(prices):
    if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        maxP = max(maxP, profit)
    else:
        l = r

    r = r + 1

print(f"{maxP}")
