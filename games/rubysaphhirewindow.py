from .basewindow import BaseWindow


class RubySapphireWindow(BaseWindow):
    def __init__(self):

        battles = [
            ("Roxanne", 15),
            ("Brawly", 18),
            ("Wattson", 23),
            ("Flannery", 28),
            ("Norman", 31),
            ("Winona", 33),
            ("Tate and Liza", 42),
            ("Wallace", 43),
            ("Steven", 58)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No Legendaries",
        ]

        super().__init__("Ruby/Sapphire", battles, optional_rules)