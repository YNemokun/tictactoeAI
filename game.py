"""
Try running the module
"""

import tictactoe

trials = 20

print("AI vs AI")
print(tictactoe.AI_AI(trials))

print("random vs random")
print(tictactoe.random_generate(trials))

print("AI vs random")
print(tictactoe.AI_random(trials))

print("random vs AI")
print(tictactoe.random_AI(trials))

# print("\nAI vs Human")
# print(tictactoe.AI_human())
