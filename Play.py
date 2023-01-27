import random
# list = [1, 2, 1, 4, 1]
# current_score = 0
#
# for i in list:
#     print(list[i])

# if 1 or 5 in list:
#     for i in range(1, len(list)):
#         if list.index(i) == 1:
#             current_score += 100
#     #print("You have a scoring roll!")
#     #print(list)
#         elif i == 5:
#             current_score += 50
# else:
#     print(list)
#     print("You Farkled! Better luck next time")
#
# print(current_score)

# initial_roll = {}
#
# def roll_dice():
#     die1 = random.randint(1, 5)
#     initial_roll.update({"die1": die1})
#     die2 = random.randint(1, 5)
#     initial_roll.update({"die2": die2})
#     die3 = random.randint(1, 5)
#     initial_roll.update({"die3": die3})
#     die4 = random.randint(1, 5)
#     initial_roll.update({"die4": die4})
#     die5 = random.randint(1, 5)
#     initial_roll.update({"die5": die5})
#
# roll_dice()
# # print(initial_roll)
#
# if initial_roll.values() == 1 or initial_roll.values() == 5:
#     print(initial_roll.values())

##want a player a round and a score in a dictionary
round_info = {}
round_info["Player Info"] = ["Player Name"]
round_info["Round"] = ["Round"]
round_info["Score"] = ["Score"]

print(round_info)