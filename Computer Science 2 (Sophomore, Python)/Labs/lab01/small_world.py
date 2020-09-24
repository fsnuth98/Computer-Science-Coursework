"""
  CSC102 - Lab 01
  Part 2 - Small World
  Franklin Nuth
  Rasul Rasulov
  January 19th, 2018
"""

world = [ ['.', '.', 'C', 'R', 'C'],
          ['C', '.', '.', 'R', '.'],
          ['R', '.', 'R', '.', '.'],
          ['C', '.', 'R', '.', 'R'],
          ['R', '.', '.', 'C', 'C'] ]


def showWorld(w, player_row, player_col):
    for row in range(len(w)):
        for col in range(len(w[0])):
            if row == player_row and col == player_col:
                print('P', end = ' ') # show player
            else:
                print(w[row][col], end = ' ') # show world item
        print()
    print()

def readAction():
    print("Enter UP, DOWN, LEFT, RIGHT to move around")
    print("Enter QUIT to end program")
    a = input("Enter action: ")    
    return a

# Tracking location of player
player_row = 0
player_col = 0

# Game loop
done = False
while not done:
    showWorld(world, player_row, player_col)
    action = readAction()
    if action == 'UP':
        if world[player_row-1][player_col]=="R":
            print("Ouch! Can't move there... there is a rock!")
        else:
            player_row -= 1
        pass
    elif action == 'DOWN':
        if world[player_row+1][player_col]=="R":
            print("Ouch! Can't move there... there is a rock!")
        else:
            player_row += 1
        pass
    elif action == 'LEFT':
        if world[player_row][player_col-1]=="R":
            print("Ouch! Can't move there... there is a rock!")   
        else:
            player_col -= 1
        pass
    elif action == 'RIGHT':
        if world[player_row][player_col+1]=="R":
            print("Ouch! Can't move there... there is a rock!")        
        else:
            player_col += 1
        pass
    elif action == 'QUIT':
        done = True
    else:
        print("\nHuh? Try again.\n")
    