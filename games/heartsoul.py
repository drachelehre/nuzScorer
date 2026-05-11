from .basewindow import BaseWindow


class HeartSoulWindow(BaseWindow):
    def __init__(self):

        battles = [
            ("Faulkner", 13),
            ("Bugsy", 17),
            ("Whitney", 13),
            ("Morty", 25),
            ("Chuck", 31),
            ("Jasmine", 35),
            ("Pryce", 34),
            ("Claire", 41),
            ("Will", 42),
            ("Koga", 44),
            ("Bruno", 46),
            ("Karen", 47),
            ("Champ", 50),
            ("Brock", 54),
            ("Misty", 54),
            ("Lt. Surge", 53),
            ("Erika", 56),
            ("Sabrina", 55),
            ("Janine", 50),
            ("Blaine", 59),
            ("Blue", 60),
            ("Red", 81)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over",
            "No held items",
        ]

        super().__init__("Heart Gold/Soul Silver", battles, optional_rules)
