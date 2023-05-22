#Import Modules
import random
from players import Player

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
def first_go():
    choice = random.randint(1,2)
    return choice


#draw() = draws board
#first_go() = randomly picks between players one and two to start
#create_players() = creates players one and two along with their names and scores.

def main():
    print("Hi! Welcome to a TicTacToe.")
    player_count = 0
    while player_count <2:
        if player_count == 1:
            playertwo = Player(player_count)
            player_count += 1
            print(player_count)
        elif player_count == 0:
            playerone = Player(player_count)
            player_count += 1
            print(player_count)
    print(f"Score are currently:\n{playerone.name} : {playerone.score}\n{playertwo.name} : {playertwo.score}")
    if first_go() == 1:
        print(f"{playerone.name} goes first!")
    else:
        print(f"{playertwo.name} goes first!")
    print("Here is the board:")
    draw()
    
main()