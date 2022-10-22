#solve board using backltracking
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

#check validity of number
def valid(board, num, pos):
    #check row col
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

#find empty box
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

#check board validity
def checkBoard(board):
    #check dup in row col
    for i in range(9):
        row = []
        for j in range(9):
            if board[i][j] != 0:
                if board[i][j] in row:
                    return False
                else:
                    row.append(board[i][j])
    for i in range(9):
        column = []
        for j in range(9):
            if board[j][i] != 0:
                if board[j][i] in column:
                    return False
                else:
                    column.append(board[j][i])

    #check dup in box
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = []
            for k in range(3):
                for l in range(3):
                    if board[i+k][j+l] != 0:
                        if board[i+k][j+l] in box:
                            return False
                        else:
                            box.append(board[i+k][j+l])
    return True