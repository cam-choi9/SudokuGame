board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

# recursive backtracking algorithm - 
# 1. Find an empty spot where value == 0
# 2. Insert a number that is valid - no overlapping number within the same row, column, and box    
# 3. Repeat steps 1 & 2 with the inserted number by calling the solve function recursively
# 4. If invalid, set the number back to 0 and try with another number
def solve(bo):

    # base case for recursive algorithm -
    # if 0 is not found, meaning the board is complete, the game ends.

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0
                
    return False


def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = "")


def find_empty(bo):
    
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    
    return None


def valid(bo, num, pos):

    # check the row if it contains the number we are inserting
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    # check the column if it contains the number we are inserting
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
        
    # check the box if it contains the number we are inserting    
    start_i = (pos[0] // 3) * 3
    start_j = (pos[1] // 3) * 3    

    for i in range(start_i, start_i + 3):
        for j in range(start_j, start_j + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


print_board(board)
solve(board)
print()
print_board(board)