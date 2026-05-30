from .basewindow import BaseWindow


class XAndYWindow(BaseWindow):
    def __init__(self):
        battles = [
            ("Viola", 12),
            ("Grant", 25),
            ("Korrina", 32),
            ("Ramos", 34),
            ("Clemont", 37),
            ("Valerie", 42),
            ("Olympia", 48),
            ("Wulfric", 59),
            ("Malva", 65),
            ("Wikstrom", 65),
            ("Drasma", 65),
            ("Siebold", 65),
            ("Diantha", 59),
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No Legendaries",
            "No Mega Evolution"
        ]

        super().__init__("X and Y", battles, optional_rules)