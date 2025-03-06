# Search a 2D Matrix
# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?


matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 10

l = (0, 0)
r = (len(matrix) - 1, len(matrix[0]))

print(l)
print(r)

ROWS, COLS = len(matrix), len(matrix[0])
top = 0
bot = ROWS - 1

while top <= bot:
    row = int((top + bot) // 2)
    if target > matrix[row][-1]:
        top = row + 1


# top_row = 0
# bottom_rows = ROWS - 1
# while top_row <= bottom_rows:
#     mid_row = int((top_row + mid_row) // 2)
#     if target > matrix[mid_row][-1]:
