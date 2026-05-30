from .basewindow import BaseWindow


class EmeraldWindow(BaseWindow):
    def __init__(self):
        battles = [
            ("Roxanne", 15),
            ("Brawly", 19),
            ("Wattson", 24),
            ("Flannery", 29),
            ("Norman", 31),
            ("Winona", 33),
            ("Tate and Liza", 42),
            ("Juan", 46),
            ("Sidney", 49),
            ("Phoebe", 51),
            ("Glacia", 53),
            ("Drake", 55),
            ("Wallace", 58)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No Legendaries",
        ]

        super().__init__("Emerald", battles, optional_rules)