import Player


game_rounds = {}
# ^^idea of holding player name, round, and score information
class Game:


    def start_game():
        num_of_players = int(input("Please enter the number of players"))
        player_names = {}
        player_number = 0
        while num_of_players > 0:
            request_names = input("Please enter player name")
            player_number += 1
            player_names.update({"Player " + str(player_number): request_names})
            num_of_players -= 1
        print(player_names)
## what if I did player # and incremented that to the number of players that would solve my key with multiple values predicament
   # def game_rounds(self):
        #I want this to increase the round number and increease the scores

