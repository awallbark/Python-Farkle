#this works for adding 1 & 5
for i in initial_roll:
    if i == 1:
        current_score += 100
    elif i == 5:
        current_score += 50
print(current_score)