"""

"""

import json


class Player:
    def __init__(self, name, piece = None):
        self.name = name
        self.wallet = 1500
        self.position = 0
        self.piece = piece
        self.properties = []

    def pay(self, payment):
        self.wallet -= payment

    def receive(self, amount):
        self.wallet += amount

    def move(self, number_of_steps):
        self.position += number_of_steps
        if self.position >= 40:
            self.position -= 40

    def get_details(self):
        return json.dumps({
            "name": self.name,
            "wallet": self.wallet,
            "position": self.position,
            "piece": self.piece,
            "properties": self.properties
        }, indent=4)
