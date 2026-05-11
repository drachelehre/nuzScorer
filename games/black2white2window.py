from .basewindow import BaseWindow


class Black2White2Window(BaseWindow):
    def __init__(self):
        battles = [
            ("Cheren", 13),
            ("Roxie", 18),
            ("Burgh", 24),
            ("Elesa", 30),
            ("Clay", 33),
            ("Skyla", 39),
            ("Drayden", 48),
            ("Marlin", 51),
            ("Shauntal", 58),
            ("Marshall", 58),
            ("Grimsley", 58),
            ("Caitlin", 58),
            ("Iris", 59),
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over"
        ]

        super().__init__("Black 2/White 2", battles, optional_rules)