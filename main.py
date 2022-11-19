import ScoreClass

#game_rounds = {"round": <value>}


turn = ScoreClass.Score()
print(turn.roll_dice())

def score_dice(dice_number):
    current_score = 0

    for k, v in dice_number.items():
        if k == "ones" and v == 1 and k == "twos" and v == 1 and k == "threes" and v == 1 and k == "fours" and v == 1 and k == "fives" and v == 1 and k == "sixes" and v == 1:
            current_score += 1500
        if k == "ones" and v == 6 or k == "twos" and v == 6 or k == "threes" and v == 6 or k == "fours" and v == 6 or k == "fives" and v == 6 or k == "sixes" and v == 6:
            current_score += 3000
        if k == "ones" and v == 5 or k == "twos" and v == 5 or k == "threes" and v == 5 or k == "fours" and v == 5 or k == "fives" and v == 5 or k == "sixes" and v == 5:
            current_score += 2000
        if k == "ones" and v == 4 or k == "twos" and v == 4 or k == "threes" and v == 4 or k == "fours" and v == 4 or k == "fives" and v == 4 or k == "sixes" and v == 4:
            current_score += 1000
        if k == "ones" and v == 3 and k == "twos" and v == 3:
            current_score += 2500
        if k == "ones" and v == 1:
            current_score += 100
        elif k == "ones" and v == 2:
            current_score += 200
        elif k == "ones" and v == 3:
            current_score += 300
        elif k == "ones" and v == 4:
            current_score += 1000
        elif k == "ones" and v == 5:
            current_score += 1500
        if k == "twos" and v == 3:
            current_score += 200
        elif k == "twos" and v == 4:
            current_score += 1000
        elif k == "twos" and v == 5:
            current_score += 1500
        if k == "threes" and v == 3:
            current_score += 300
        elif k == "threes" and v == 4:
            current_score += 1000
        elif k == "threes" and v == 5:
            current_score += 1500
        if k == "fours" and v == 3:
            current_score += 400
        elif k == "fours" and v == 4:
            current_score += 1000
        elif k == "fours" and v == 5:
            current_score += 1500
        if k == "fives" and v == 1:
            current_score += 50
        elif k == "fives" and v == 2:
            current_score += 100
        elif k == "fives" and v == 3:
            current_score += 500
        elif k == "fives" and v == 4:
            current_score += 1000
        elif k == "fives" and v == 5:
            current_score += 1500
    print(current_score)
    return current_score



    # else:
    #     if current_score == 0:
    #         print("You Farkled! Better luck next time")
    #         print(roll)

# count_dice = count_dice(turn)
# score_dice(count_dice)



