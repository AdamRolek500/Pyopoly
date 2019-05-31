"""
Space class is used to represent property spaces
"""

import json


class Space:
    def __init__(self, name, index, type):
        self.name = name
        self.index = index
        self.type = type

    def dump_details(self):
        return json.dumps({
            "name": self.name,
            "index": self.index,
            "type": self.type
        }, indent=4)

    def action(self):
        if self.type is "go":
            print("This is go!")
        elif self.type is "community-chest":
            print("community-chest")
        elif self.type is "chance":
            print("chance")
        elif self.type is "jail":
            print("jail")
        elif self.type is "free-parking":
            print("free-parking")
        elif self.type is "go-to-jail":
            print("go-to-jail")
