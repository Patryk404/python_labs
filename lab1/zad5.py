import random

board = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]

class Player:
    sign = " "
    def __init__(self, realsign):
        self.sign = realsign

def display_board():
    print("-------------")
    for x in board:
        for idy, y in enumerate(x): 
            if idy == 2:
                print("| "+y+" |")
                print("-------------")
            else:
                print("| "+y+" ",end="")

def check_win(player,computer):
    #check horizontally
    computer_counter = 0
    player_counter = 0
    for y in board:
        for x in y:
            if x == player.sign:
                player_counter += 1
            elif x == computer.sign:
                computer_counter += 1 
        if computer_counter == 3:
            print("Computer wins!")
            return True
        elif player_counter == 3:
            print("Player wins!")
            return True
        computer_counter = 0
        player_counter = 0
    
    #check vertically 
    computer_counter = 0
    player_counter = 0 
    for x in range(3):
        for y in range(3):
            if board[y][x] == player.sign:
                player_counter += 1 
            elif board[y][x] == computer.sign:
                computer_counter += 1 
        if player_counter == 3:
            print("Player wins!")
            return True
        elif computer_counter == 3:
            print("Computer wins!")
            return True  
        computer_counter = 0
        player_counter = 0

    #check diagonally
    computer_counter = 0 
    player_counter = 0 
    vertical = 0
    for y in board:
        if y[vertical] == player.sign:
            player_counter += 1
        elif y[vertical] == computer_counter:
            computer_counter += 1
        vertical += 1
    if player_counter == 3: 
        print("Player wins!")
        return True
    elif computer_counter == 3:
        print("Computer wins!")
        return True    
     
    return False


def computer_move(computer):
    x = random.randint(1,3) - 1 
    y = random.randint(1,3) - 1 
    if board[y][x] != " ":
        computer_move(computer)
    else:
        board[y][x] = computer.sign
        print("Computer did his move")
        return None        

Player1 = Player("X")
Computer = Player("O")
finish = False
while finish==False:
    x = input("Enter x pos: ")
    y = input("Enter y pos: ")
    x = int(x)-1
    y = int(y)-1
    
    if board[y][x] != " ":
        print("You can't place here your sign")
    else: 
        board[y][x] = Player1.sign
        finish = check_win(Player1,Computer)
        if finish == False:
            computer_move(Computer)

    display_board()