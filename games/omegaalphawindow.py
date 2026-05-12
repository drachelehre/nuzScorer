from .basewindow import BaseWindow


class OmegaAlphaWindow(BaseWindow):
    def __init__(self):

        battles = [
            ("Roxanne", 14),
            ("Brawly", 16),
            ("Wattson", 21),
            ("Flannery", 28),
            ("Norman", 30),
            ("Winona", 35),
            ("Tate and Liza", 45),
            ("Wallace", 46),
            ("Sidney", 52),
            ("Phoebe", 53),
            ("Glacia", 54),
            ("Drake", 55),
            ("Steven", 59)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No Mega Evolution"
        ]

        super().__init__("Ruby/Sapphire", battles, optional_rules)