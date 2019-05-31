"""
Monopoly clone with Pygame

By: Adam Rolek
"""

from property import Property
import json

GAME_BOARD = [None for i in range(40)]
properties = []

with open("spaces.json", "r") as fd:
    data = json.load(fd)
    index = 0
    for space in data:
        if space["type"] == "property":
            p = Property(space["name"], space["cost"], space["rent"], space["color"], index, space["house"], 5, space["group"], space["type"])
            properties.append(p)
            GAME_BOARD[index] = p
        index += 1
    for space in properties:
        print(space.dump_details())
        space.hello_world()





for i in range(20, 31):
    if GAME_BOARD[i] is None:
        print("X", end="")
    else:
        print("-", end="")

diff = 10
print()
for i in range(31, 40):
    diff += 2
    if GAME_BOARD[i - diff] is None:
        print("X", end="")
    else:
        print("-", end="")
    print("         ", end="")
    if GAME_BOARD[i] is None:
        print("X")
    else:
        print("-")

for i in range(10, -1, -1):
    if GAME_BOARD[i] is None:
        print("X", end="")
    else:
        print("-", end="")
