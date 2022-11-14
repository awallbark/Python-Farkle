import random


initial_roll = []
current_score = 0
#game_rounds = {"round": <value>}
ones_counter = 0
twos_counter = 0
threes_counter = 0
fours_counter = 0
fives_counter = 0
sixes_counter = 0

def roll_dice():
    die_count = 0
    while die_count <= 5:
        die = random.randint(1,6)
        initial_roll.append(die)
        die_count += 1

#first way of writing the random die
    # die1 = random.randint(1, 6)
    # initial_roll.append(die1)
    # die2 = random.randint(1, 6)
    # initial_roll.append(die2)
    # die3 = random.randint(1, 6)
    # initial_roll.append(die3)
    # die4 = random.randint(1, 6)
    # initial_roll.append(die4)
    # die5 = random.randint(1, 6)
    # initial_roll.append(die5)


roll = roll_dice()

if initial_roll.count(1) or initial_roll.count(5):
    print("You have a scoring roll!")
    print(initial_roll)
    for a in initial_roll:
        if a == 1:
            ones_counter += 1
        elif a == 2:
            twos_counter += 1
        elif a == 3:
            threes_counter += 1
        elif a == 4:
            fours_counter += 1
        elif a == 5:
            fives_counter += 1
        elif a == 6:
            sixes_counter += 1
    if ones_counter == 1:
        current_score += 100
    elif ones_counter == 2:
        current_score += 200
    elif ones_counter == 3:
        current_score += 300
    elif ones_counter == 4:
        current_score += 1000
    elif ones_counter == 5:
        current_score += 2000
    elif ones_counter == 6:
        current_score += 3000
    if twos_counter == 3:
        current_score += 200
    elif twos_counter == 4:
        current_score += 1000
    elif twos_counter == 5:
        current_score += 2000
    elif twos_counter == 6:
        current_score += 3000
    if threes_counter == 3:
        current_score += 300
    elif threes_counter == 4:
        current_score += 1000
    elif threes_counter == 5:
        current_score += 2000
    elif threes_counter == 6:
        current_score += 3000
    if fours_counter == 3:
        current_score += 400
    elif fours_counter == 4:
        current_score += 1000
    elif fours_counter == 5:
        current_score += 2000
    elif fours_counter == 6:
        current_score += 3000
    if fives_counter == 1:
        current_score += 50
    elif fives_counter == 2:
        current_score += 100
    elif fives_counter == 3:
        current_score += 500
    elif fives_counter == 4:
        current_score += 1000
    elif fives_counter == 5:
        current_score += 2000
    elif fives_counter == 6:
        current_score += 3000
    if sixes_counter == 3:
        current_score += 600
    elif sixes_counter == 4:
        current_score += 1000
    elif sixes_counter == 5:
        current_score += 2000
    elif sixes_counter == 6:
        current_score += 3000
else:
    if current_score == 0:
        print("You Farkled! Better luck next time")
        print(initial_roll)

print(current_score)


