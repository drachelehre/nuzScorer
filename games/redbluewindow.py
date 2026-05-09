from PyQt6.QtWidgets import (QWidget, QLabel, QCheckBox, QLineEdit, QPushButton,
                            QMessageBox, QGridLayout, QSpinBox)


class RedBlueWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Red/Blue")

        layout = QGridLayout()

        # Header row
        layout.addWidget(QLabel("Battle"), 0, 0)
        layout.addWidget(QLabel("Max Level"), 0, 1)
        layout.addWidget(QLabel("Your Level"), 0, 2)

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

        self.gym_widgets = []

        for row, (battle, max_level) in enumerate(battles, start=1):

            checkbox = QCheckBox(battle)

            level_label = QLabel(str(max_level))

            spinbox = QSpinBox()
            spinbox.setRange(1, 100)

            layout.addWidget(checkbox, row, 0)
            layout.addWidget(level_label, row, 1)
            layout.addWidget(spinbox, row, 2)

            # Store references if needed later
            self.gym_widgets.append({
                "name": battle,
                "checkbox": checkbox,
                "max_level": max_level,
                "spinbox": spinbox
            })

        self.setLayout(layout)

    def calculate(self):
        self.total = 0