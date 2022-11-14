import random


roll = []
current_score = 0
#game_rounds = {"round": <value>}
dice_number = {}

def roll_dice():
    die_count = 0
    while die_count <= 5:
        die = random.randint(1, 6)
        roll.append(die)
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


turn = roll_dice()

def count_dice(turn):
    ones_counter = 0
    twos_counter = 0
    threes_counter = 0
    fours_counter = 0
    fives_counter = 0
    sixes_counter = 0
    if roll.count(1) or roll.count(5) or roll.count(2) >= 3 or roll.count(3) >= 3 or roll.count(4) >= 3 or roll.count(6) >= 3:
        print("You have a scoring roll!")
        print(roll)
        for a in roll:
            if a == 1:
                ones_counter += 1
                dice_number.update({"ones": ones_counter})
            elif a == 2:
                twos_counter += 1
                dice_number.update({"twos": twos_counter})
            elif a == 3:
                threes_counter += 1
                dice_number.update({"threes": threes_counter})
            elif a == 4:
                fours_counter += 1
                dice_number.update({"fours": fours_counter})
            elif a == 5:
                fives_counter += 1
                dice_number.update({"fives": fives_counter})
            elif a == 6:
                sixes_counter += 1
                dice_number.update({"sixes": sixes_counter})
        print(dice_number)
            # if ones_counter == 1:
            #     current_score += 100
            # elif ones_counter == 2:
            #     current_score += 200
            # elif ones_counter == 3:
            #     current_score += 300
            # elif ones_counter == 4:
            #     current_score += 1000
            # elif ones_counter == 5:
            #     current_score += 2000
            # elif ones_counter == 6:
            #     current_score += 3000
            # if twos_counter == 3:
            #     current_score += 200
            # elif twos_counter == 4:
            #     current_score += 1000
            # elif twos_counter == 5:
            #     current_score += 2000
            # elif twos_counter == 6:
            #     current_score += 3000
            # if threes_counter == 3:
            #     current_score += 300
            # elif threes_counter == 4:
            #     current_score += 1000
            # elif threes_counter == 5:
            #     current_score += 2000
            # elif threes_counter == 6:
            #     current_score += 3000
            # if fours_counter == 3:
            #     current_score += 400
            # elif fours_counter == 4:
            #     current_score += 1000
            # elif fours_counter == 5:
            #     current_score += 2000
            # elif fours_counter == 6:
            #     current_score += 3000
            # if fives_counter == 1:
            #     current_score += 50
            # elif fives_counter == 2:
            #     current_score += 100
            # elif fives_counter == 3:
            #     current_score += 500
            # elif fives_counter == 4:
            #     current_score += 1000
            # elif fives_counter == 5:
            #     current_score += 2000
            # elif fives_counter == 6:
            #     current_score += 3000
            # if sixes_counter == 3:
            #     current_score += 600
            # elif sixes_counter == 4:
            #     current_score += 1000
            # elif sixes_counter == 5:
            #     current_score += 2000
            # elif sixes_counter == 6:
            #     current_score += 3000
    else:
        if current_score == 0:
            print("You Farkled! Better luck next time")
            print(roll)

count_dice(turn)
print(current_score)


