def find_next_empty(puzzle):

    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c

    return None,None        

def is_valid(puzzle,guess,row,col):
    row_vals=puzzle[row] #for rows
    if guess in row_vals:
        return False
    
    #col_vals=[]
    #for i in range(1,10):
     #   col_vals.append(puzzle[i][col])
    col_vals=[puzzle[i][col] for i in range(9)]  #for columns
    if guess in col_vals:
        return False
      
    #for 3x3 sub-blocks
    row_start=(row//3)*3
    col_start=(col//3)*3

    for r in range(row_start,row_start+3):
        for c in range (col_start,col_start+3):
            if guess==puzzle[r][c]:
                return False
            

            
    return True

def solve_sudoku(puzzle):
    row,col=find_next_empty(puzzle)
    if row==None: #found a solution
        return True
    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col]=guess
            if solve_sudoku(puzzle):
                return True
              
        #if our guess is not valid or it does not solve the puzzle than we need to backtrack  
          
        puzzle[row][col]=-1

    return False
if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)

    




                                                                            



