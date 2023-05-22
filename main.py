#Import Modules
import random
from players import Player

player_count = 1

#Create the TicTacToe board
def draw():
    board = ''

    for i in range(-1,6):

        if i%2==0:
            board += '|      ' * 4
            board += '\n|      |      |      |'

        else:
            board += ' _____ ' * 3

        board += '\n'
    print (board)

#Randomly picks who goes first
def first_go(playerone_name, playertwo_name):
    choice = random.randint(1,2)
    return choice


#draw() = draws board
#first_go() = randomly picks between players one and two to start
#create_players() = creates players one and two along with their names and scores.

def main():
    print("Hi! Welcome to a TicTacToe.")
    playerone = Player(player_count)
    playertwo = Player(player_count)
    if first_go() == 1:
        print(f"{playerone.name} goes first!")
    else:
        print(f"{playertwo.name} goes first!")
    print("Here is the board:")
    draw()
    
main()