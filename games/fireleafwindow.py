from .basewindow import *


class FireLeafWindow(BaseWindow):
    def __init__(self):
        battles = [
            ("Brock", 14),
            ("Misty", 21),
            ("Lt. Surge", 24),
            ("Erika", 29),
            ("Koga", 43),
            ("Sabrina", 43),
            ("Blaine", 47),
            ("Giovanni", 50),
            ("Lorelei", 56),
            ("Bruno", 58),
            ("Agatha", 60),
            ("Lance", 62),
            ("Champ", 63)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over"
        ]

        super().__init__("Fire Red/Leaf Green", battles, optional_rules)