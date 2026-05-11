from .basewindow import *


class DiamondPearlWindow(BaseWindow):
    def __init__(self):
        battles = [
            ("Roark", 14),
            ("Gardenia", 22),
            ("Fantima", 26),
            ("Maylene", 32),
            ("Crasher Wake", 37),
            ("Byron", 41),
            ("Candice", 44),
            ("Volkner", 50),
            ("Aaron", 53),
            ("Bertha", 55),
            ("Flint", 57),
            ("Lucian", 59),
            ("Cynthia", 62)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over"
        ]

        super().__init__("Diamond/Pearl", battles, optional_rules)