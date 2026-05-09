from PyQt6.QtWidgets import (
    QWidget, QLabel, QCheckBox, QPushButton,
    QGridLayout, QSpinBox, QVBoxLayout,
    QScrollArea
)


class YellowWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yellow")

        # Main layout for the window
        main_layout = QVBoxLayout(self)

        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        # Container widget inside the scroll area
        container = QWidget()

        # Your existing grid layout
        layout = QGridLayout(container)

        # Header row
        layout.addWidget(QLabel("Battle"), 0, 0)
        layout.addWidget(QLabel("Max Level"), 0, 1)
        layout.addWidget(QLabel("Your Level"), 0, 2)

        battles = [
            ("Brock", 12),
            ("Misty", 21),
            ("Lt. Surge", 24),
            ("Erika", 32),
            ("Koga", 50),
            ("Sabrina", 50),
            ("Blaine", 54),
            ("Giovanni", 55),
            ("Lorelei", 56),
            ("Bruno", 58),
            ("Agatha", 60),
            ("Lance", 62),
            ("Champ", 65)
        ]

        optional_rules = [
            "Gym level cap",
            "Minimum battles",
            "No items",
            "Limit Pokemon Centers",
            "White-Out is Game Over"
        ]

        self.battle_widgets = []

        for row, (battle, max_level) in enumerate(battles, start=1):

            checkbox = QCheckBox(battle)

            level_label = QLabel(str(max_level))

            your_level = QSpinBox()
            your_level.setRange(1, 100)

            layout.addWidget(checkbox, row, 0)
            layout.addWidget(level_label, row, 1)
            layout.addWidget(your_level, row, 2)

            self.battle_widgets.append({
                "checkbox": checkbox,
                "max_level": max_level,
                "your_level": your_level
            })

        self.rule_widgets = []

        self.rule_label = QLabel("Optional rules:")
        layout.addWidget(self.rule_label, 14, 0)

        start_row = 15

        for index, rule in enumerate(optional_rules):
            checkbox = QCheckBox(rule)

            row = start_row + (index // 3)
            col = index % 3

            layout.addWidget(checkbox, row, col)

            self.rule_widgets.append(checkbox)

        self.death_score_label = QLabel("Number of deaths:")
        layout.addWidget(self.death_score_label, 17, 0)

        self.death_score = QSpinBox()
        self.death_score.setRange(0, 100)
        layout.addWidget(self.death_score, 17, 1)

        self.calculate_button = QPushButton("Calculate...")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button, 18, 2)

        self.score_label = QLabel("Score:")
        layout.addWidget(self.score_label, 18, 0)

        self.total_label = QLabel("0")
        layout.addWidget(self.total_label, 18, 1)

        # Put container into scroll area
        scroll.setWidget(container)

        # Add scroll area to main window
        main_layout.addWidget(scroll)

        self.resize(500, 400)

    def calculate(self):
        total = 0

        for battle in self.battle_widgets:

            won = battle['checkbox'].isChecked()
            gym_level = battle['max_level']
            your_level = battle['your_level'].value()

            if won:
                total += (10 + (gym_level - your_level))

        for rule in self.rule_widgets:
            if rule.isChecked():
                total *= 1.1

        total -= (self.death_score.value() * 5)

        total = max(0, int(total))

        self.total_label.setText(str(total))