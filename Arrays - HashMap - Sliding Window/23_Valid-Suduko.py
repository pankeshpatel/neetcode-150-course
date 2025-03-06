# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.


Input = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

validSudukoFlag = True


# checking rows in Suduko Array
for row in range(0, 9):
    validSet = set()
    for i in range(0, 9):
        if Input[row][i] == ".":
            continue
        if Input[row][i] in validSet:
            validSudukoFlag = False
        else:
            validSet.add(Input[row][i])

# checking cols in Suduko Array
for col in range(0, 9):
    validSet = set()
    for i in range(0, 9):
        if Input[i][col] == ".":
            continue
        if Input[i][col] in validSet:
            validSudukoFlag = False
        else:
            validSet.add(Input[i][col])


for square in range(0, 9):
    validSet = set()
    for i in range(0, 3):
        for j in range(0, 3):
            row = (square // 3) * 3 + i
            col = (square % 3) * 3 + j
            if Input[row][col] == ".":
                continue
            if Input[row][col] in validSet:
                validSudukoFlag = False
            else:
                validSet.add(Input[row][col])

print(f"{validSudukoFlag}")
