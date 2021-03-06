N, M = 6, 7
grid = []

#This function prints the grid of Connect Four Game as the game progresses
def print_grid():
    print("Player 1: X  vs  Player 2: O")
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * M + '--')

#This function checks if row or column or diagonal is full with same characters
def check_win():
    #If row is full with same characters, 
    #the game is over and the player with that character has won
    for i in range(N):
        for j in range(M-3):
            s = {grid[i][j], grid[i][j+1], grid[i][j+2], grid[i][j+3]}
            if grid[i][j] != '.' and len(s) == 1:
                return True
    #If column is full with same characters, 
    #the game is over and the player with that character has won
    for j in range(N-3):
        for i in range(M):
            s = {grid[j][i], grid[j+1][i], grid[j+2][i], grid[j+3][i]}
            if grid[j][i] != '.' and len(s) == 1:
                return True
    #If diagonal is full with same characters, 
    #the game is over and the player with that character has won
    for i in range(N-3):
        for j in range(M-3):
            s = {grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]}
            if grid[i][j] != '.' and len(s) == 1:
                return True
    #If diagonal is full with same characters, 
    #the game is over and the player with that character has won
    for i in range(N-3):
        for j in range(3, M):
            s = {grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3]}
            if grid[i][j] != '.' and len(s) == 1:
                return True
    #Otherwise, there isn't a win state in the game, 
    #if all cases above not reached
    return False

#This function checks if row or column or diagonal is full with same characters
def check_tie(mark):
    #If row a single type of characters
    for i in range(N):
        for j in range(M-3):
            s = {mark, grid[i][j], grid[i][j+1], grid[i][j+2], grid[i][j+3]}
            if '.' in s and len(s) == 2:
                return False
    #If column a single type of characters
    for j in range(N-3):
        for i in range(M):
            s = {mark, grid[j][i], grid[j+1][i], grid[j+2][i], grid[j+3][i]}
            if '.' in s and len(s) == 2:
                return False
    #If diagonal a single type of characters
    for i in range(N-3):
        for j in range(M-3):
            s = {mark, grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]}
            if '.' in s and len(s) == 2:
                return False
    #If diagonal a single type of characters
    for i in range(N-3):
        for j in range(3, M):
            s = {mark, grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3]}
            if '.' in s and len(s) == 2:
                return False
    #Otherwise, there isn't a win state in the game, 
    #if all cases above not reached
    return True

#This function checks if given cell is empty or not 
def check_empty(i):
    return grid[0][i] == '.'

#This function checks if given position is valid or not 
def check_valid_column(i):
    return 0 <= i < M

#This function sets a value to a cell
def set_cell(i, mark):
    for j in range(N-1, -1, -1):
        if grid[j][i] == '.':
            grid[j][i] = mark
            break

#This function clears the grid
def grid_clear():
    global grid
    grid = [['.'] * M for i in range(N)]


#MAIN FUNCTION
def play_game():
    print("Connect Four Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'X' if player == 0 else 'O'
        #Read an input from the player
        print('Player %s' % mark)
        i = int(input('Enter the column index: '))
        while not check_valid_column(i) or not check_empty(i):
            i = int(input('Enter a valid column index: '))
        #Set the input position with the mark
        set_cell(i, mark)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % mark)
            break
        op_mark = 'O' if player == 0 else 'X'
        #Check if the state of the grid has a tie state
        if check_tie(op_mark):
            #Prints the grid
            print_grid()
            print("Woah! That's a tie!")
            break		
        #Player number changes after each turn
        player = 1 - player 


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
