#Create Players
PLAYERS = 1
class Player:
    
    def __init__(self, player_count):
        if player_count == 1:
            print('Player One')
        else:
            print('Player Two')
        self.name = input('Please enter the players name: \n')
        self.score = 0
        player_count += 1
        if player_count == 2:
            player_count = 1
    