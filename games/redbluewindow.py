from .basewindow import BaseWindow


class RedBlueWindow(BaseWindow):
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
            ("Champ", 65)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No Legendaries",
        ]

        super().__init__("Red/Blue", battles, optional_rules)
