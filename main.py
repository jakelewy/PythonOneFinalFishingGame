"""
main.py: the only and only main file for the game
-----

"""

### Global vars
# List for fishing rods
#* TODO: turn into dict with "rod name": [rodPower, basePrice]
g_fishingRods = [
    "Plastic Rod", # ID: 0
    "Metal Rod",   # ID: 1
    "Silver Rod",  # ID: 2
    "Golden Rod",  # ID: 3
    "Diamond Rod", # ID: 4
    "Obsidian Rod" # ID: 5
]
# List of baits + bait power (1-10)
#* TODO: turn into dict with "bait name": [baitPower, basePrice]
g_baits = {
    "Plastic": 1,     # ID: 0
    "Trash": 2,       # ID: 1
    "Worm": 3,        # ID: 2
    "Bait Ball": 5,   # ID: 3
    "Super Bait": 6,  # ID: 4
    "Tasty Bait": 8,  # ID: 5
    "Golden Worm": 10 # ID: 6
}
# List of all the fish you can catch + their rarity (#(%) chance)
g_fish = {
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
    "": 0, # ID: 0
}

### CLASSES
# The player class is where all of the progress and data is stored
class Player:
    def __init__(self, coins, currentBait, unlockedBaits, currentRod, unlockedRods, catchHistory):
        
        pass


# Function to return a dict of player stats
def getDefaultState():
    """
    Docstring for getDefaultState
    """
    return {
        "coins": 0,
        "fishingRodsUnlocked": [],
        "currentRod": g_fishingRods[0]

    }

def main():
    """
    Docstring for main
    """
    # Main game loop
    while True:
        print()