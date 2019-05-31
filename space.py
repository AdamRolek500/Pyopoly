"""
Space class is used to represent property spaces
"""

import json


class Space:
    def __init__(self, name, index, type, price=None, group=None, rent=None, color=None, house_cost=None, mortgage=None,
                 owner=None):
        self.name = name
        self.index = index
        self.type = type
        self.price = price
        self.rent = rent
        self.color = color
        self.house_cost = house_cost
        self.mortgage = mortgage
        self.group = group
        self.owner = owner

    def get_details(self):
        details = {
            "name": self.name,
            "type": self.type,
            "index": self.index
        }
        if self.type == "go" or self.type == "community-chest" or self.type == "chance" or self.type == "jail" or \
                self.type == "free-parking" or self.type == "go-to-jail":
            return json.dumps(details, indent=4)
        elif self.type == "tax":
            details["cost"] = self.price
            return json.dumps(details, indent=4)
        elif self.type == "railroad":
            details["cost"] = self.price
            details["group"] = self.group
            return json.dumps(details, indent=4)
        elif self.type == "property":
            details["cost"] = self.price
            details["rent"] = self.rent
            details["color"] = self.color
            details["group"] = self.group
            details["house_cost"] = self.house_cost
            details["mortgage"] = self.mortgage
            details["owner"] = self.owner
            return json.dumps(details, indent=4)
        else:
            return json.dumps(details, indent=4)

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
