"""
Monopoly clone with Pygame

By: Adam Rolek
"""

from space import Space

GAME_BOARD = [40]

s = Space("Boardwalk", 400, (50, 200, 600, 1400, 1700, 2000), "blue", 39, 200, 200)
print(s.dump_details())
