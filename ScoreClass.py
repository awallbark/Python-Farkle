import random


class Score():
    # game_rounds = {"round": <value>}

    # def __init__(self):
    #      score = self.score


    def roll_dice(self):
        roll = []
        die_count = 0
        while die_count <= 5:
            die = random.randint(1, 6)
            roll.append(die)
            die_count += 1
        return roll


    def count_dice(self, roll):
        dice_number = {}
        ones_counter = 0
        twos_counter = 0
        threes_counter = 0
        fours_counter = 0
        fives_counter = 0
        sixes_counter = 0
        if roll.count(1) or roll.count(5) or roll.count(2) >= 3 or roll.count(3) >= 3 or roll.count(4) >= 3 or roll.count(
                6) >= 3:
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
        else:
                print("You Farkled! Better luck next time")
                print(roll)
        return dice_number

    def score_dice(self, arg):
        current_score = 0

        for k, v in arg.items():
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