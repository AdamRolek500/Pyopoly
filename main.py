"""
Monopoly clone with Pygame

By: Adam Rolek
"""

from space import Space
from player import Player
from PIL import ImageTk
import PIL
from tkinter import *
import json
import random
import tkinter
import logging

GAME_BOARD = [None for i in range(40)]
properties = []
# TODO: Implement logging where there are prints
logging.basicConfig(filename="Pyopoly.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2


class Board:
    def __init__(self):
        print("Initializing Board Object...")
        self.root = tkinter.Tk()

        self.board_image = ImageTk.PhotoImage(file = "monopoly_board.jpg")
        self.board = Canvas(self.root, bg="blue", height=self.board_image.height(), width=self.board_image.width())
        self.board.pack(expand = YES, fill = BOTH)
        self.canvas_board_image = self.board.create_image(0, 0, image = self.board_image, anchor = NW)
        self.board.bind("<Configure>", self.resize_image)

        self.GAME_BOARD = []

        with open("spaces.json", "r") as fd:
            data = json.load(fd)
            index = 0
            for space in data:
                if space["type"] == "property":
                    # Space(self, name, index, type, price, group, rent, color, house_cost, mortgage, owner)
                    p = Space(space["name"], index, space["type"], space["cost"], space["group"], space["rent"],
                            space["color"], space["house"], 5)
                elif space["type"] == "tax":
                    p = Space(space["name"], index, space["type"], space["cost"])
                elif space["type"] == "railroad":
                    p = Space(space["name"], index, space["type"], space["cost"], space["group"])
                else:
                    p = Space(space["name"], index, space["type"])
                self.GAME_BOARD.append(p)
                index += 1
            # Printing out space information
            # for space in self.GAME_BOARD:
            #     try:
            #         print(space.get_details())
            #     except Exception as error:
            #         print(error)


        # Running the mainloop
        self.run()

    def resize_image(self, event):
        img = PIL.Image.open("monopoly_board.jpg").resize(
            (event.width, event.height), PIL.Image.ANTIALIAS
        )
        self.board_image = ImageTk.PhotoImage(img)
        self.board.itemconfig(self.canvas_board_image, image=self.board_image)

    def run(self):
        self.root.mainloop()
        

def main():
    board = Board()

    # play = Player("Adam", 1)
    # with open("spaces.json", "r") as fd:
    #     data = json.load(fd)
    #     index = 0
    #     for space in data:
    #         if space["type"] == "property":
    #             # Space(self, name, index, type, price, group, rent, color, house_cost, mortgage, owner)
    #             p = Space(space["name"], index, space["type"], space["cost"], space["group"], space["rent"],
    #                       space["color"], space["house"], 5)
    #             p.set_owner(play)
    #         elif space["type"] == "tax":
    #             p = Space(space["name"], index, space["type"], space["cost"])
    #             p.set_owner(play)
    #         elif space["type"] == "railroad":
    #             p = Space(space["name"], index, space["type"], space["cost"], space["group"])
    #             p.set_owner(play)
    #         else:
    #             p = Space(space["name"], index, space["type"])
    #         GAME_BOARD[index] = p
    #         index += 1
    #     for space in GAME_BOARD:
    #         try:
    #             print(space.get_details())
    #         except Exception as error:
    #             print(error)

    # #while True:
    # die1, die2 = roll_dice()
    # print("die1: " + str(die1) + "\ndie2: " + str(die2))
    # play.move((die1 + die2))
    # print(play.get_details())
    # input("Press Enter to continue...")

    # for i in range(20, 31):
    #     if GAME_BOARD[i] is None:
    #         print("X", end="")
    #     else:
    #         print("-", end="")
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
    
    # for i in range(10, -1, -1):
    #     if GAME_BOARD[i] is None:
    #         print("X", end="")
    #     else:
    #         print("-", end="")


if __name__ == "__main__":
    main()
