import random

initial_roll = []
current_score = []
roll = []

def roll_dice():
    die1 = random.randint(1, 5)
    initial_roll.append(die1)
    die2 = random.randint(1, 5)
    initial_roll.append(die2)
    die3 = random.randint(1, 5)
    initial_roll.append(die3)
    die4 = random.randint(1, 5)
    initial_roll.append(die4)
    die5 = random.randint(1, 5)
    initial_roll.append(die5)

roll = roll_dice()
if 1 in initial_roll:
    print("You have a scoring roll!")
    print(initial_roll)
elif 5 in initial_roll:
    print("You have a scoring roll!")
    print(initial_roll)
else:
    print(initial_roll)
    print("You Farkled! Better luck next time")



