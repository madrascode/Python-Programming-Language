N = 15
a_row = 5
grid = []

#This function prints the grid of Gomoku as the game progresses
def print_grid():
    print("Player 1: B  vs  Player 2: W")
    print('--' + '---' * N + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * N + '--')

#This function checks if row or column or diagonal is full with same characters
def check_win():
    pass

#This function checks if row or column or diagonal is full with same characters
def check_tie(mark):
    pass

#This function checks if given cell is empty or not 
def check_empty(i, j):
    pass

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    pass

#This function sets a value to a cell
def set_cell(i, j, mark):
    pass

#This function clears the grid
def grid_clear():
    pass


#MAIN FUNCTION
def play_game():
    print("Gomoku Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'B' if player == 0 else 'W'
        #Read an input from the player
        print('Player %s' % mark)
        i, j = map(int, input('Enter the row index and column index: ').split())
        while not check_valid_position(i, j) or not check_empty(i, j):
            i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
        #Set the input position with the mark
        set_cell(i, j, mark)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % mark)
            break
        #Check if the state of the grid has a tie state
        if check_tie(mark):
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
