"""

"""

import json
from space import Space


class Property(Space):
    def __init__(self, name, price, rent, color, index, house_cost, mortgage, group, type):
        Space.__init__(self, name, index, type)
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
