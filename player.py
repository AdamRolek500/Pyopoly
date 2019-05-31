"""

"""

import json


class Player:
    def __init__(self, name, id, piece = None):
        self.name = name
        self.id = id
        self.wallet = 1500
        self.position = 0
        self.piece = piece

    def pay(self, payment):
        self.wallet -= payment

    def receive(self, amount):
        self.wallet += amount

    def move(self, number_of_steps):
        self.position += number_of_steps
        if self.position >= 40:
            self.position -= 40

    def get_id(self):
        return self.id

    def get_details(self):
        return json.dumps({
            "name": self.name,
            "wallet": self.wallet,
            "position": self.position,
            "piece": self.piece
        }, indent=4)
