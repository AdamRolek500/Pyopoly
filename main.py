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
import time
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
        self.root.attributes("-fullscreen", True)
        self.root.bind('<Escape>', self.close)
        self.root_frame = Frame(self.root, bg="red")
        self.root_frame.pack(side=LEFT)

        self.board_frame = Frame(self.root_frame, bg="green")
        self.board_frame.pack(side=LEFT)
        self.board_image = ImageTk.PhotoImage(file = "monopoly_board.jpg")
        self.board_canvas = Canvas(self.board_frame, bg="blue", height=self.board_image.height(), width=self.board_image.width())
        self.canvas_board_image = self.board_canvas.create_image(0, 0, image=self.board_image, anchor = NW)
        # self.board_canvas.bind("<Configure>", self.resize_image)
        self.board_canvas.pack()
        self.resize_image()

        self.information_frame = Frame(self.root_frame, bg="yellow")
        self.board_frame.pack(side=RIGHT)

        # b = Button(self.board, text="hey")
        # b.pack()

        self.GAME_BOARD = []

        # with open("spaces.json", "r") as fd:
        #     data = json.load(fd)
        #     index = 0
        #     for space in data:
        #         if space["type"] == "property":
        #             # Space(self, name, index, type, price, group, rent, color, house_cost, mortgage, owner)
        #             p = Space(space["name"], index, space["type"], space["cost"], space["group"], space["rent"],
        #                     space["color"], space["house"], 5)
        #         elif space["type"] == "tax":
        #             p = Space(space["name"], index, space["type"], space["cost"])
        #         elif space["type"] == "railroad":
        #             p = Space(space["name"], index, space["type"], space["cost"], space["group"])
        #         else:
        #             p = Space(space["name"], index, space["type"])
        #         self.GAME_BOARD.append(p)
        #         index += 1
            # Printing out space information
            # for space in self.GAME_BOARD:
            #     try:
            #         print(space.get_details())
            #     except Exception as error:
            #         print(error)


        # Running the mainloop
        self.run()

    def resize_image(self):
        height = self.root.winfo_screenheight()
        img = PIL.Image.open("monopoly_board.jpg").resize(
            (height, height), PIL.Image.ANTIALIAS
        )
        self.board_image = ImageTk.PhotoImage(img)
        self.board_canvas.itemconfig(self.canvas_board_image, image=self.board_image)
        self.board_canvas.config(width=height, height=height)

    def run(self):
        self.root.mainloop()

    def close(self, event):
        screen_height, screen_width = self.root.winfo_screenheight(), self.root.winfo_screenwidth()
        width, height = 200, 300
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        newWindow = tkinter.Toplevel(self.root)
        newWindow.title("quit menu")
        newWindow.geometry("{}x{}+{}+{}".format(width, height, int(x), int(y)))

        Label(newWindow, text ="This is a new window").pack()

        newWindow.transient(self.root)
        newWindow.focus_set()
        newWindow.grab_set()
        self.root.wait_window(newWindow)

        
        

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
