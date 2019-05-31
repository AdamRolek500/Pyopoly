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
    with open("spaces.json", "r") as fd:
        data = json.load(fd)
        index = 0
        for space in data:
            if space["type"] == "property":
                # Space(name, index, type, price, rent, color, house_cost, mortgage, group)
                p = Space(space["name"], index, space["type"], space["cost"], space["rent"], space["color"],
                          space["house"],
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

    play = Player("Adam")
    
    die1, die2 = roll_dice()
    print("die1: " + str(die1) + "\ndie2: " + str(die2))
    play.move((die1 + die2))
    print(play.get_details())

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
