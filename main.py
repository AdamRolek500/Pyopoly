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
        # Creating the root window
        self.root = tkinter.Tk() 
        # Making the root window fullscreen
        self.root.attributes("-fullscreen", True)
        # Binding the ESCAPE key to the close function
        self.root.bind('<Escape>', self.close)
        # Creating the root frame for the game and packing to the left
        self.root_frame = Frame(self.root, bg="red")
        self.root_frame.pack(side=LEFT)

        # Creating the board frame (board_frame is in the root frame)
        self.board_frame = Frame(self.root_frame, bg="green")
        self.board_frame.pack(side=LEFT)
        # broad_img is the picture of the monopoly board
        self.board_image = ImageTk.PhotoImage(file = "monopoly_board.jpg")
        # board_canvas contains the pictures and controls
        self.board_canvas = Canvas(self.board_frame, bg="blue", height=self.board_image.height(), width=self.board_image.width())
        # Setting the top left corner of the board to (0, 0)
        self.canvas_board_image = self.board_canvas.create_image(0, 0, image=self.board_image, anchor = NW)
        # Packing the canvas and sizing the board img
        self.board_canvas.pack()
        self.resize_image()

        # Placing clickable spaces on the board
        self.place_spaces()



            # if space["type"] == "property":
            #     p = Space(space["name"], index, space["type"], space["cost"], space["group"], space["rent"], space["color"], space["house"], 5)
            # elif space["type"] == "tax":
            #     p = Space(space["name"], index, space["type"], space["cost"])
            # elif space["type"] == "railroad":
            #     p = Space(space["name"], index, space["type"], space["cost"], space["group"])
            # else:
            #     p = Space(space["name"], index, space["type"])
            # self.spaces.append(p)
            # index += 1


            # Printing out space information
            # for space in self.spaces:
            #     try:
            #         print(space.get_details())
            #     except Exception as error:
            #         print(error)

        
        self.information_frame = Frame(self.root_frame, bg="yellow")
        self.board_frame.pack(side=RIGHT)

        # Running the mainloop
        self.run()

    def find_space(self, id):
        for space in self.spaces:
            if space.get_id() == id:
                return space

    def get_space_info(self, event):
        space = self.find_space(event.widget.find_withtag('current')[0])
        print(space.get_details())

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

    def quit_confirm(self):
        self.root.destroy()

    def quit_cancel(self):
        self.quit_window.destroy()

    def close(self, event):
        screen_height, screen_width = self.root.winfo_screenheight(), self.root.winfo_screenwidth()
        width, height = 200, 200
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.quit_window = tkinter.Toplevel(self.root)
        self.quit_window.title("quit menu")
        self.quit_window.geometry("{}x{}+{}+{}".format(width, height, int(x), int(y)))

        Button(self.quit_window, text ="Close", command=self.quit_confirm).pack()
        Button(self.quit_window, text ="Cancle", command=self.quit_cancel).pack()

        self.quit_window.transient(self.root)
        self.quit_window.focus_set()
        self.quit_window.grab_set()
        self.root.wait_window(self.quit_window)

    def place_spaces(self):
        with open("spaces.json", "r") as fd:
            self.spaces = []
            length = self.root.winfo_screenheight()
            space_length = int(length * (1.75/13.25))
            space_width = int(length * (1.089/13.25))
            row_length = 0
            img = PIL.Image.open("button.png").resize(
                (space_length, space_length), PIL.Image.ANTIALIAS
            )
            photo = ImageTk.PhotoImage(img)
            space_data = json.load(fd)
            index = 0
            # Setting up the button for Go
            space = space_data[index]
            space_image_button = self.board_canvas.create_image(length - space_length,length - space_length,image=photo, anchor=NW)
            self.board_canvas.tag_bind(space_image_button, "<Button-1>", self.get_space_info)
            self.spaces.append(Space(space["name"], index, space["type"], space_id=space_image_button))
            # Account the the width of Go
            row_length += space_length
            index += 1

            # Placing the spaces on the bottum row
            img = PIL.Image.open("button.png").resize(
                (space_width, space_length), PIL.Image.ANTIALIAS
            )
            photo = ImageTk.PhotoImage(img)
            for i in range(9):
                # Account the the width of Go
                row_length += space_width
                space = space_data[index]
                space_image_button = self.board_canvas.create_image(length - row_length,length - space_length,image=photo, anchor=NW)
                self.board_canvas.tag_bind(space_image_button, "<Button-1>", self.get_space_info)
                self.spaces.append(Space(space["name"], index, space["type"], space_id=space_image_button))
                index += 1

            # Placing the Jail space
            img = PIL.Image.open("button.png").resize(
                (space_length, space_length), PIL.Image.ANTIALIAS
            )
            photo = ImageTk.PhotoImage(img)
            space = space_data[index]
            space_image_button = self.board_canvas.create_image(0,length - space_length,image=photo, anchor=NW)
            self.board_canvas.tag_bind(space_image_button, "<Button-1>", self.get_space_info)
            self.spaces.append(Space(space["name"], index, space["type"], space_id=space_image_button))
            row_length = space_length
            index += 1

            # Placing the spaces on the LEFT row
            img = PIL.Image.open("button.png").resize(
                (space_length, space_width), PIL.Image.ANTIALIAS
            )
            photo = ImageTk.PhotoImage(img)
            for i in range(9):
                # Account the the width of Go
                row_length += space_width
                space = space_data[index]
                space_image_button = self.board_canvas.create_image(0,length - row_length,image=photo, anchor=NW)
                self.board_canvas.tag_bind(space_image_button, "<Button-1>", self.get_space_info)
                self.spaces.append(Space(space["name"], index, space["type"], space_id=space_image_button))
                index += 1

            # Placing the Jail space
            img = PIL.Image.open("button.png").resize(
                (space_length, space_length), PIL.Image.ANTIALIAS
            )
            photo = ImageTk.PhotoImage(img)
            space = space_data[index]
            space_image_button = self.board_canvas.create_image(0,0,image=photo, anchor=NW)
            self.board_canvas.tag_bind(space_image_button, "<Button-1>", self.get_space_info)
            self.spaces.append(Space(space["name"], index, space["type"], space_id=space_image_button))
            row_length = space_length
            index += 1

            # Placing the spaces on the TOP row
            img = PIL.Image.open("button.png").resize(
                (space_width, space_length), PIL.Image.ANTIALIAS
            )
            photo = ImageTk.PhotoImage(img)
            for i in range(9):
                space = space_data[index]
                space_image_button = self.board_canvas.create_image(row_length,0,image=photo, anchor=NW)
                self.board_canvas.tag_bind(space_image_button, "<Button-1>", self.get_space_info)
                self.spaces.append(Space(space["name"], index, space["type"], space_id=space_image_button))
                # Account the the width of Go
                row_length += space_width
                index += 1

            # Placing the Jail space
            img = PIL.Image.open("button.png").resize(
                (space_length, space_length), PIL.Image.ANTIALIAS
            )
            photo = ImageTk.PhotoImage(img)
            space = space_data[index]
            space_image_button = self.board_canvas.create_image(length - space_length,0,image=photo, anchor=NW)
            self.board_canvas.tag_bind(space_image_button, "<Button-1>", self.get_space_info)
            self.spaces.append(Space(space["name"], index, space["type"], space_id=space_image_button))
            row_length = space_length
            index += 1

            # Placing the spaces on the RIGHT row
            img = PIL.Image.open("button.png").resize(
                (space_length, space_width), PIL.Image.ANTIALIAS
            )
            photo = ImageTk.PhotoImage(img)
            for i in range(9):
                space = space_data[index]
                space_image_button = self.board_canvas.create_image(length - space_length,row_length,image=photo, anchor=NW)
                self.board_canvas.tag_bind(space_image_button, "<Button-1>", self.get_space_info)
                self.spaces.append(Space(space["name"], index, space["type"], space_id=space_image_button))
                # Account the the width of Go
                row_length += space_width
                index += 1

        
        

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
