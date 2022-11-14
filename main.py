import random


initial_roll = [1, 1, 1, 1, 1, 1]
current_score = 0
game_rounds = []
ones_counter = 0
twos_counter = 0
threes_counter = 0
fours_counter = 0
fives_counter = 0
sixes_counter = 0

# def roll_dice():
#     die1 = random.randint(1, 6)
#     initial_roll.append(die1)
#     die2 = random.randint(1, 6)
#     initial_roll.append(die2)
#     die3 = random.randint(1, 6)
#     initial_roll.append(die3)
#     die4 = random.randint(1, 6)
#     initial_roll.append(die4)
#     die5 = random.randint(1, 6)
#     initial_roll.append(die5)


#roll = roll_dice()
if 1 or 5 in initial_roll:
    print("You have a scoring roll!")
    print(initial_roll)
    for i in initial_roll:
        if i == 1:
            ones_counter += 1
            #current_score += 100
        elif i == 2:
            twos_counter += 1
        elif i == 3:
            threes_counter += 1
        elif i == 4:
            fours_counter += 1
        elif i == 5:
            fives_counter += 1
        elif i == 6:
            sixes_counter += 1
            #current_score += 50
    if ones_counter == 1:
        current_score += 100
    elif ones_counter == 2:
        current_score += 200
    elif ones_counter == 3:
        current_score += 300
    elif ones_counter == 4:
        current_score += 1000
    elif ones_counter == 5:
        current_score == 2000
    elif ones_counter == 6:
        current_score += 3000
else:
    print(initial_roll)
    print("You Farkled! Better luck next time")

print(current_score)


