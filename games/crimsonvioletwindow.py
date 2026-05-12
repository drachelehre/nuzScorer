from .basewindow import BaseWindow


class CrimsonVioletWindow(BaseWindow):
    def __init__(self):
        battles = [
            ("Katy", 15),
            ("Klawf (Titan)", 16),
            ("Brassius", 18),
            ("Bombirdier (Titan)", 20),
            ("Giacomo", 21),
            ("Iono", 24),
            ("Mela", 27),
            ("Orthworm (Titan)", 29),
            ("Kofu", 30),
            ("Atticus", 33),
            ("Larry", 36),
            ("Ryme", 42),
            ("Tulip", 45),
            ("Great Tusk/Iron Treads", 45),
            ("Grusha", 48),
            ("Ortega", 51),
            ("Eri", 56),
            ("Tatsugiri & Dondozo", 57),
            ("Rika", 58),
            ("Poppy", 59),
            ("Larry (E4)", 60),
            ("Hassel", 61),
            ("Geeta", 62),
            ("Arven", 63),
            ("Penny", 63),
            ("AI Sado/Turo", 67)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No Terastalizing"
        ]

        super().__init__("Crimson/Violet", battles, optional_rules)