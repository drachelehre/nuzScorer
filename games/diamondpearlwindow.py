from .basewindow import BaseWindow


class DiamondPearlWindow(BaseWindow):
    def __init__(self):
        battles = [
            ("Roark", 14),
            ("Gardenia", 22),
            ("Maylene", 30),
            ("Crasher Wake", 30),
            ("Fantima", 36),
            ("Byron", 39),
            ("Candice", 42),
            ("Volkner", 49),
            ("Aaron", 57),
            ("Bertha", 59),
            ("Flint", 61),
            ("Lucian", 63),
            ("Cynthia", 66)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over"
            "No Legendaries",
        ]

        super().__init__("Diamond/Pearl", battles, optional_rules)