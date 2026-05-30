from .basewindow import BaseWindow


class BlackWhiteWindow(BaseWindow):
    def __init__(self):
        battles = [
            ("Chili/Cilan/Cress", 14),
            ("Lenore", 20),
            ("Burgh", 23),
            ("Elesa", 27),
            ("Clay", 31),
            ("Skyla", 35),
            ("Brycen", 39),
            ("Iris/Drayden", 43),
            ("Shauntal", 50),
            ("Marshall", 50),
            ("Grimsley", 50),
            ("Caitlin", 50),
            ("N", 52),
            ("Ghetsis", 54)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No Legendaries",
        ]

        super().__init__("Black/White", battles, optional_rules)