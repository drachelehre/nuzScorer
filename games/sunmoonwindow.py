from .basewindow import BaseWindow


class SunMoonWindow(BaseWindow):
    def __init__(self):
        battles = [
            ("Raticate/Gumshoos", 12),
            ("Hala", 15),
            ("Wishiwashi", 20),
            ("Salazzle", 22),
            ("Lurantis", 24),
            ("Olivia", 27),
            ("Vikavolt", 29),
            ("Mimikyu", 33),
            ("Nanu", 39),
            ("Kommo-o", 45),
            ("Hapu", 48),
            ("Hala (E4)", 55),
            ("Olivia (E4)", 55),
            ("Acerola", 55),
            ("Kahili", 55),
            ("Kukui", 58)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No Z Moves"
        ]

        super().__init__("Sun/Moon", battles, optional_rules)