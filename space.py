"""
Space class is used to represent property spaces
"""

import json


class Space:
    def __init__(self, name, price, rent, color, index, house_cost, mortgage):
        self.name = name
        self.price = price
        self.rent = rent
        self.color = color
        self.index = index
        self.house_cost = house_cost
        self.mortgage = mortgage

    def dump_details(self):
        return json.dumps({
            "name": self.name,
            "price": self.price,
            "rent": self.rent,
            "color": self.color,
            "index": self.index,
            "house_cost": self.house_cost,
            "mortgage": self.mortgage
        }, indent=4)
