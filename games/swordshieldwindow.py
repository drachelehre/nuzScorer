from .basewindow import BaseWindow


class SwordShieldWindow(BaseWindow):
    def __init__(self):

        battles = [
            ("Milo", 20),
            ("Nessa", 24),
            ("Kabu", 27),
            ("Bea/Alister", 36),
            ("Opal", 38),
            ("Gordi/Melony", 42),
            ("Piers", 46),
            ("Raihan", 48),
            ("Marnie", 49),
            ("Hop", 49),
            ("Bede", 53),
            ("Nessa (Finals)", 53),
            ("Bea/Alister (Finals)", 54),
            ("Raihan (Finals)", 55),
            ("Leon", 65)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No Legendaries",
            "No Dynamaxing/Gigantamaxing"
        ]

        super().__init__("Sword/Shield", battles, optional_rules)