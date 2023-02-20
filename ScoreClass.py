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


    def complex_scoring(self, arg):
        score = 0
        dice_count_triplets = 0
        dice_count_pairs = 0
        #dice_count_four_of_a_kind_and_a_pair = 0

        for v in arg.values():
            if v == 6:
                score += 3000
                break
            elif v == 5:
                score += 2000
            elif v == 4 and v == 2:
                score += 1500
            elif v == 4:
                score = 1000
            elif v == 3:
                dice_count_triplets += 1
                while dice_count_triplets < 2:
                    if v == 3:
                        dice_count_triplets += 1
                if dice_count_triplets == 2:
                    score += 1500
            elif v == 2:
                dice_count_pairs += 1
                while dice_count_pairs < 3:
                    if v == 2:
                        dice_count_pairs += 1
                if dice_count_pairs == 3:
                    score += 1500

            return score

    def score_dice(self, arg):
        current_score = 0

        for k, v in arg.items():
            #Straight 1 of each number
            if k == "ones" and v == 1 and k == "twos" and v == 1 and k == "threes" and v == 1 and k == "fours" and v == 1 and k == "fives" and v == 1 and k == "sixes" and v == 1:
                current_score += 1500
                #six of a kind
            # if v == 6:
            #     current_score += 3000
            #     #five of a kind
            # if v == 5:
            #     current_score += 2000
            #     #four of a kind
            # if v == 4:
            #     current_score += 1000
            # if k == "ones" and v == 3 and k == "twos" and v == 3:
            #     current_score += 2500
            if k == "ones" and v == 1:
                current_score += 100
            elif k == "ones" and v == 2:
                current_score += 200
            if k == "twos" and v == 3:
                current_score += 200
            if k == "threes" and v == 3:
                current_score += 300
            if k == "fours" and v == 3:
                current_score += 400
            if k == "fives" and v == 1:
                current_score += 50
            elif k == "fives" and v == 2:
                current_score += 100
            elif k == "fives" and v == 3:
                current_score += 500
                current_score += 3000
            if k == "sixes" and v == 3:
                current_score += 600
        print(current_score)
        return current_score

   #stuff i played around with at work
   # for k, v in dice_number.items():
   #     if k == "ones COunt" and v == 1:
   #         score = 100
   #     elif k == "ones COunt" and v == 2:
   #         score = 200
   #     elif k == "Ones Count" and v == 3:
   #         score = 300
   #     elif k == "ones count" and v == 4:
   #         score = 1000
   #     elif k == "ones count" and v == 5:
   #         score = 2000
   #     elif k == "ones count" and v == 6:
   #         score = 3000

    # for k, v in dice_roll.items():
    #     if v == 1:
    #         ones_counter +=1
    #     elif v == 2:
    #         twos_counter +=1
    #     elif v ==3:
    #         threes_counter +=1
    #     elif v == 4:
    #         fours_counter += 1
    #     elif v == 5:
    #         fives_counter +=1
    #     elif v == 6:
    #         sixs_counter +=1
    #     score_dice.update({"ones": ones_counter...etc})