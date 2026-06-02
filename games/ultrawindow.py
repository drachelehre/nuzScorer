from .basewindow import BaseWindow


class UltraWindow(BaseWindow):
    def __init__(self):
        battles = [
            ("Raticate/Gumshoos", 12),
            ("Hala", 16),
            ("Araquanid", 20),
            ("Marowak", 22),
            ("Lurantis", 24),
            ("Olivia", 28),
            ("Togedemaru", 33),
            ("Mimikyu", 35),
            ("Nanu", 44),
            ("Kommo-o", 49),
            ("Hapu", 54),
            ("Hau", 60)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No Legendaries",
            "No Z Moves"
        ]

        super().__init__("Ultra Sun/Ultra Moon", battles, optional_rules)