"""
Monopoly clone with Pygame

By: Adam Rolek
"""

from space import Space
from player import Player
import json
import random

GAME_BOARD = [None for i in range(40)]
properties = []


def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2


def main():
    play = Player("Adam", 1)
    with open("spaces.json", "r") as fd:
        data = json.load(fd)
        index = 0
        for space in data:
            if space["type"] == "property":
                # Space(self, name, index, type, price, group, rent, color, house_cost, mortgage, owner)
                p = Space(space["name"], index, space["type"], space["cost"], space["group"], space["rent"],
                          space["color"], space["house"], 5)
                p.set_owner(play)
            elif space["type"] == "tax":
                p = Space(space["name"], index, space["type"], space["cost"])
                p.set_owner(play)
            elif space["type"] == "railroad":
                p = Space(space["name"], index, space["type"], space["cost"], space["group"])
                p.set_owner(play)
            else:
                p = Space(space["name"], index, space["type"])
            GAME_BOARD[index] = p
            index += 1
        for space in GAME_BOARD:
            try:
                print(space.get_details())
            except Exception as error:
                print(error)

    #while True:
    die1, die2 = roll_dice()
    print("die1: " + str(die1) + "\ndie2: " + str(die2))
    play.move((die1 + die2))
    print(play.get_details())
    input("Press Enter to continue...")

    # for i in range(20, 31):
    #     if GAME_BOARD[i] is None:
    #         print("X", end="")
    #     else:
    #         print("-", end="")
    #
    # diff = 10
    # print()
    # for i in range(31, 40):
    #     diff += 2
    #     if GAME_BOARD[i - diff] is None:
    #         print("X", end="")
    #     else:
    #         print("-", end="")
    #     print("         ", end="")
    #     if GAME_BOARD[i] is None:
    #         print("X")
    #     else:
    #         print("-")
    #
    # for i in range(10, -1, -1):
    #     if GAME_BOARD[i] is None:
    #         print("X", end="")
    #     else:
    #         print("-", end="")


if __name__ == "__main__":
    main()
