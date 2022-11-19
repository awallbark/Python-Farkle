import Player


# game_rounds = {"round": <value>}
# ^^idea of holding player name, round, and score information
class Game:

    def start_game():
        num_of_players = int(input("Please enter the number of players"))
        player_names = {}
        while num_of_players > 0:
            request_names = input("Please enter player name")
            player_names.update({"Player": request_names})
            num_of_players -= 1
        print(player_names)
