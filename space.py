"""
Space class is used to represent property spaces
"""

import json


class Space:
    def __init__(self, name, index, space_type, price=None, group=None, rent=None, color=None, house_cost=None, mortgage=None, owner=None, space_id=None):
        self.name = name
        self.index = index
        self.type = space_type
        self.price = price
        self.rent = rent
        self.color = color
        self.house_cost = house_cost
        self.mortgage = mortgage
        self.group = group
        self.owner = owner
        self.space_id = space_id

    def get_id(self):
        return self.space_id

    def get_details(self):
        return {
            "name": self.name,
            "index": self.index,
            "type": self.type,
            "price": self.price,
            "rent": self.rent,
            "color": self.color,
            "house_cost": self.house_cost,
            "mortgage": self.mortgage,
            "group": self.group,
            "owner": self.owner,
            "space_id": self.space_id
        }

    def action(self):
        if self.type == "go":
            print("This is go!")
        elif self.type == "community-chest":
            print("community-chest")
        elif self.type == "chance":
            print("chance")
        elif self.type == "jail":
            print("jail")
        elif self.type == "free-parking":
            print("free-parking")
        elif self.type == "go-to-jail":
            print("go-to-jail")
        elif self.type == "tax":
            print("tax")
        elif self.type == "railroad":
            print("railroad")
        elif self.type == "property":
            print(self.name + "\t" + self.color)
        else:
            print("Unknown")

    def set_owner(self, player):
        self.owner = player.get_id()
