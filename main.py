import Game
import ScoreClass


# new_game = Game.Game
# new_game.start_game()



turn = ScoreClass.Score()
roll = turn.roll_dice()
count = turn.count_dice(roll)
complex_scoring = turn.complex_scoring(count)
#scoring = turn.score_dice(count)print(roll)
print(count)
print(complex_scoring)







# count_dice = count_dice(turn)
# score_dice(count_dice)



