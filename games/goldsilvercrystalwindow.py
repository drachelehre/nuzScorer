from .basewindow import *


class GoldSilverCrystalWindow(BaseWindow):
    def __init__(self):

        battles = [
            ("Faulkner", 9),
            ("Misty", 16),
            ("Whitney", 20),
            ("Morty", 25),
            ("Chuck", 30),
            ("Jasmine", 35),
            ("Pryce", 31),
            ("Claire", 40),
            ("Will", 42),
            ("Koga", 44),
            ("Bruno", 46),
            ("Karen", 47),
            ("Champ", 50),
            ("Brock", 44),
            ("Misty", 47),
            ("Lt. Surge", 45),
            ("Erika", 46),
            ("Sabrina", 48),
            ("Janine", 39),
            ("Blaine", 50),
            ("Blue", 58),
            ("Red", 81)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No held items",
        ]

        super().__init__("Gold/Silver/Crystal", battles, optional_rules)
