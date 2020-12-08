import tictactoe
import csv
import pandas as pd

trials = 100
runs = 100


def count_winners(winners):
    x = winners.count("X")
    o = winners.count("O")
    return {"X wins": x, "O wins": o, "Draw": trials - x - o}


# Load winners
# with open('ar_winners.csv','w') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Winners"])

# run = runs
# while run > 0:
#     run -= 1
#     result = tictactoe.AI_random(trials)
#     with open('ar_winners.csv','a', newline='') as file:
#         writer = csv.writer(file)
#
#         for player in result:
#             writer.writerow(player)
#
# print(result)

# Load data
# # AI & random
# with open('AI_random.csv', 'w', newline='') as file:
#     fieldnames = ['X wins', 'O wins', "Draw"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#     writer.writeheader()
#
run = runs
while run > 0:
    run -= 1
    result_ar = count_winners(tictactoe.AI_random(trials))
    with open('AI_random.csv', 'a', newline='') as file:
        fieldnames = ['X wins', 'O wins', "Draw"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(result_ar)

#
# # AI & AI
# with open('AI_AI.csv', 'w', newline='') as file:
#     fieldnames = ['X wins', 'O wins', "Draw"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#     writer.writeheader()
#
run = runs
while run > 0:
    run -= 1
    result_aa = count_winners(tictactoe.AI_AI(trials))
    with open('AI_AI.csv', 'a', newline='') as file:
        fieldnames = ['X wins', 'O wins', "Draw"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(result_aa)

#
# # random & random
# with open('random_random.csv', 'w', newline='') as file:
#     fieldnames = ['X wins', 'O wins', "Draw"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#     writer.writeheader()
#
run = runs
while run > 0:
    run -= 1
    result_rr = count_winners(tictactoe.random_generate(trials))
    with open('random_random.csv', 'a', newline='') as file:
        fieldnames = ['X wins', 'O wins', "Draw"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(result_rr)


# random & AI
# with open('random_AI.csv', 'w', newline='') as file:
#     fieldnames = ['X wins', 'O wins', "Draw"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#     writer.writeheader()

run = runs
while run > 0:
    run -= 1
    result_ra = count_winners(tictactoe.random_AI(trials))
    with open('random_AI.csv', 'a', newline='') as file:
        fieldnames = ['X wins', 'O wins', "Draw"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(result_ra)

# display averages:
print("AI_random")
data = pd.read_csv("AI_random.csv")
print(data.mean())

print("AI_AI")
data = pd.read_csv("AI_AI.csv")
print(data.mean())

print("random_random")
data = pd.read_csv("random_random.csv")
print(data.mean())

print("random_AI")
data = pd.read_csv("random_AI.csv")
print(data.mean())

