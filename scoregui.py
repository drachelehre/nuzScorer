from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                            QMessageBox, QGridLayout, QMainWindow, QComboBox, QSpinBox)
from games.redbluewindow import *
from games.yellowwindow import *


class ScoreGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nuzlocke Scorer")

        layout = QGridLayout()

        game_select_label = QLabel("Game Select:")

        self.game_select = QComboBox()
        self.game_select.addItems([
            'RB', 'Yellow', 'GSC', 'RS', 'Emerald' 'FRLG',
            'DP', 'Platinum', 'HGSS', 'BW', 'B2W2', 'XY',
            'SM', 'USUM', 'SwSh', 'CV'
        ])

        layout.addWidget(game_select_label, 0, 0)
        layout.addWidget(self.game_select, 0, 1)

        choose_button = QPushButton("Choose...")
        choose_button.clicked.connect(self.choose_game)

        layout.addWidget(choose_button, 1, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def choose_game(self):
        game = self.game_select.currentText()

        match game:
            case 'RB':
                print("Red/Blue chosen")
                self.w = RedBlueWindow()
                self.w.show()

            case 'Yellow':
                print("Yellow chosen")
                self.w = YellowWindow()
                self.w.show()

            case 'GSC':
                print('Gold/Silver/Crystal')

            case _:
                print(f"{game} chosen")
