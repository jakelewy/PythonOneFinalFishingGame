"""
main.py: the only and only main file for the game
-----

"""

###! GLOBALS

# List for fishing rods
# dict with "rod name": [rodPower (1-10), basePrice]
g_fishingRods = {
    "Plastic Rod": [2, 0], # ID: 0
    "Metal Rod": [3, 10],   # ID: 1
    "Silver Rod": [5, 35],  # ID: 2
    "Golden Rod": [6, 57],  # ID: 3
    "Diamond Rod": [8, 85], # ID: 4
    "Obsidian Rod": [10, 172], # ID: 5
}

# List of baits + bait power (1-10)
# dict with "bait name": [baitPower, basePrice]
g_baits = {
    "Plastic": [1, 0],     # ID: 0
    "Trash": [2, 4],       # ID: 1
    "Worm": [3, 12],        # ID: 2
    "Bait Ball": [5, 23],   # ID: 3
    "Super Bait": [6, 35],  # ID: 4
    "Tasty Bait": [8, 47],  # ID: 5
    "Golden Worm": [10, 72] # ID: 6
}

# Dict of fish
"""
g_fish["RARITY"]["FISH"] = baseCoinsForFish

Rarities:
- Trash
- Common
- Uncommon
- Rare
"""
#* TODO: Add more fish
g_fish = {
    "TRASH": {
        # For example, Driftwood has a base coin price of 2
        "Driftwood": 1,
        "Seaweed": 1,
        "Pile Of Sticks": 2,
        "Rock": 2,
    },
    "COMMON": {
        "Peeper": 3,
        "Perch": 3,
        "Clownfish": 4,
        "Doubloon": 0
    },
    "UNCOMMON": {
        "Gold Nugget": 5,
        "Salmon": 5,
        "Bluegill": 6,
        "Special Stone": 6
    },
    "RARE": {
        "Werid Orb": 7,
        "Golden Clownfish": 8,
        "Shiny Worm": 9,
        "Diamond": 10
    }
}

###! CLASSES
# The player class is where all of the progress and data is stored
class Player:
    # Making sure to set deaults for variable info (that way to set default player just call 'Player()')
    def __init__(self, coins=0, currentBait=g_baits[0], unlockedBaits=[g_baits[0]], currentRod=g_fishingRods[0], unlockedRods=[g_fishingRods[0]], catchHistory=[]):
        self.coins = coins
        self.currentBait = currentBait
        self.unlockedBaits = unlockedBaits
        self.currentRod = currentRod
        self.unlockedRods = unlockedRods
        self.catchHistory = catchHistory

###! HELPERS
def printMainLine():
    print("Welcome Player, To the Ultimate Fishing Game!")

def printHome():
    print("--HOME--")
    print("[1]: Go Fish")
    print("[2]: Go To Shop")
    print(">>> ")

def printPlayerInfo(playerInfo: Player):
    print("--INFO--")
    print(f"Coins: {playerInfo.coins}")
    print(f"Total Catches: {len(playerInfo.catchHistory)}")

def printFishMenu(playerObj: Player, ):
    # Tell the player how to fish + tell them rod and bait they're using
    pass

# Main function
def main():
    """
    Docstring for main
    """
    # Create player
    player = Player()
    # Main game loop
    #* TODO: Implement basic game loop
    while True:
        printMainLine()
        printPlayerInfo(player)
        printHome()
        userInput = int(input()) # not putting anything in params for input because '>>> ' is already printed

        # Fish
        if userInput == 1:
            pass
        
        # Shop (Shop handles inventory)
        if userInput == 2:
            pass