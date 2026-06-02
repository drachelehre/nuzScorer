from .basewindow import BaseWindow


class YellowWindow(BaseWindow):
    def __init__(self):

        battles = [
            ("Brock", 12),
            ("Misty", 21),
            ("Lt. Surge", 24),
            ("Erika", 32),
            ("Koga", 50),
            ("Sabrina", 50),
            ("Blaine", 54),
            ("Giovanni", 55),
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

        super().__init__("Yellow", battles, optional_rules)