from PyQt6.QtWidgets import (
    QWidget, QLabel, QCheckBox, QPushButton,
    QGridLayout, QSpinBox, QVBoxLayout,
    QScrollArea
)


class BaseWindow(QWidget):

    def __init__(self, title, battles, optional_rules):
        super().__init__()

        self.setWindowTitle(title)

        # Main layout
        main_layout = QVBoxLayout(self)

        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        # Container inside scroll area
        container = QWidget()

        # Grid layout
        layout = QGridLayout(container)

        # Header row
        layout.addWidget(QLabel("Battle"), 0, 0)
        layout.addWidget(QLabel("Max Level"), 0, 1)
        layout.addWidget(QLabel("Your Level"), 0, 2)

        self.battle_widgets = []

        # Battles
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

        # Optional rules
        self.rule_widgets = []

        rule_label_row = len(battles) + 1
        rules_start_row = rule_label_row + 1

        self.rule_label = QLabel("Optional rules:")
        layout.addWidget(self.rule_label, rule_label_row, 0)

        for index, rule in enumerate(optional_rules):

            checkbox = QCheckBox(rule)

            row = rules_start_row + (index // 3)
            col = index % 3

            layout.addWidget(checkbox, row, col)

            self.rule_widgets.append(checkbox)

        # Bottom section
        bottom_row = rules_start_row + ((len(optional_rules) - 1) // 3) + 2

        self.death_score_label = QLabel("Number of deaths:")
        layout.addWidget(self.death_score_label, bottom_row, 0)

        self.death_score = QSpinBox()
        self.death_score.setRange(0, 100)
        layout.addWidget(self.death_score, bottom_row, 1)

        self.score_label = QLabel("Score:")
        layout.addWidget(self.score_label, bottom_row + 1, 0)

        self.total_label = QLabel("0")
        layout.addWidget(self.total_label, bottom_row + 1, 1)

        self.calculate_button = QPushButton("Calculate...")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button, bottom_row + 1, 2)

        # Scroll area setup
        scroll.setWidget(container)

        main_layout.addWidget(scroll)

        self.resize(500, 600)

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

        total -= self.death_score.value()

        total = max(0, int(total))

        self.total_label.setText(str(total))
