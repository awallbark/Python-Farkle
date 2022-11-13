import random


initial_roll = []
current_score = 0
game_rounds = []

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
if 1 or 5 in initial_roll:
    print("You have a scoring roll!")
    print(initial_roll)
    for i in initial_roll:
        if i == 1:
            current_score += 100
        elif i == 5:
            current_score += 50
else:
    print(initial_roll)
    print("You Farkled! Better luck next time")

print(current_score)


