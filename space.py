"""
Space class is used to represent property spaces
"""

import json


class Space:
    def __init__(self, name, index, type, price=None, rent=None, color=None, house_cost=None, mortgage=None, group=None):
        self.name = name
        self.index = index
        self.type = type
        self.price = price
        self.rent = rent
        self.color = color
        self.house_cost = house_cost
        self.mortgage = mortgage
        self.group = group

    def dump_details(self):
        return json.dumps({
            "name": self.name,
            "price": self.price,
            "rent": self.rent,
            "color": self.color,
            "type": self.type,
            "group": self.group,
            "index": self.index,
            "house_cost": self.house_cost,
            "mortgage": self.mortgage
        }, indent=4)

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
            print("property")
        else:
            print("Unknown")
