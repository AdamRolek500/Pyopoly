"""
Monopoly clone with Pygame

By: Adam Rolek
"""

from space import Space
import json

GAME_BOARD = [None for i in range(40)]
properties = []

with open("spaces.json", "r") as fd:
    data = json.load(fd)
    index = 0
    for space in data:
        if space["type"] == "property":
            # Space(name, index, type, price, rent, color, house_cost, mortgage, group)
            p = Space(space["name"], index, space["type"], space["cost"], space["rent"], space["color"], space["house"],
                      5, space["group"])
        else:
            p = Space(space["name"], index, space["type"])
        GAME_BOARD[index] = p
        index += 1
    for space in GAME_BOARD:
        try:
            space.action()
        except Exception as error:
            print(error)





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
