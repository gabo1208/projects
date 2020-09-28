input = [[".", ".", ".", ".", ".", ".", "5", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], ["9", "3", ".", ".", "2", ".", "4", ".", "."], [".", ".", "7", ".",
                                                                                                                                                                                                      ".", ".", "3", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "3", "4", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "."], [".", ".", ".", ".", ".", "5", "2", ".", "."]]
for row in input:
    print(row)

for r, c in enumerate(input):
    print(r)
    print(c)


def validateRow(board, i):
    counter = [0] * 10
    for j in range(9):
        if board[i][j] != '.':
            if counter[int(board[i][j])] > 0:
                return False
            else:
                counter[int(board[i][j])] += 1
    return True


def validateCol(board, j):
    counter = [0] * 10
    for i in range(9):
        if board[i][j] != '.':
            if counter[int(board[i][j])] > 0:
                return False
            else:
                counter[int(board[i][j])] += 1
    return True


def validateBox(board, i, j):
    counter = [0] * 10
    for x in range(i * 3, (i * 3) + 3):
        for y in range(j * 3, (j * 3) + 3):
            if board[x][y] != '.':
                if counter[int(board[x][y])] > 0:
                    return False
                else:
                    counter[int(board[x][y])] += 1
    return True


def isValidSudoku(board):
    rows = [False] * 9
    cols = [False] * 9
    box1 = [False] * 3
    box2 = [False] * 3
    box3 = [False] * 3
    boxes = [box1, box2, box3]

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                valid = True
                if not rows[i]:
                    rows[i] = validateRow(board, i)
                    valid = rows[i]
                if not cols[j]:
                    cols[j] = validateCol(board, j)
                    valid &= cols[j]
                if not boxes[i // 3][j // 3]:
                    boxes[i // 3][j // 3] = validateBox(board, i // 3, j // 3)
                    valid &= boxes[i // 3][j // 3]
                if not valid:
                    return False
    return True


print(isValidSudoku(input))
