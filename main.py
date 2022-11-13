import random

initial_score_dice = []
current_score = []
roll = []

def roll_dice():
    die1 = random.randint(1, 5)
    initial_score_dice.append(die1)
    die2 = random.randint(1, 5)
    initial_score_dice.append(die2)
    die3 = random.randint(1, 5)
    initial_score_dice.append(die3)
    die4 = random.randint(1, 5)
    initial_score_dice.append(die4)
    die5 = random.randint(1, 5)
    initial_score_dice.append(die5)

roll = roll_dice()
for i in initial_score_dice:
    if initial_score_dice.index(i) == 1 or initial_score_dice.index(i) == 5:
        print("You have a scoring roll!")
        print(initial_score_dice)
        break
    else:
        print(initial_score_dice)
        print("You Farkled! Better luck next time")
        break



