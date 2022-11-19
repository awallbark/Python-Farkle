import random


class Score():


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


    def count_dice(roll):
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
            print(dice_number)
            return dice_number
