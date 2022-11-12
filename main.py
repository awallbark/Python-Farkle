import random

score_dice = []

def roll_dice():
    die = random.randint(1, 5)
    return die

number_of_times_rolled = 0

while number_of_times_rolled < 5:
    roll = roll_dice()
    score_dice.append(roll)
    number_of_times_rolled += 1

print(score_dice)



