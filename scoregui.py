from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QGridLayout, QMainWindow, QComboBox
)

from games.redbluewindow import RedBlueWindow
from games.yellowwindow import YellowWindow
from games.goldsilvercrystalwindow import GoldSilverCrystalWindow
from games.rubysaphhirewindow import RubySapphireWindow
from games.emeraldwindow import EmeraldWindow
from games.diamondpearlwindow import DiamondPearlWindow
from games.platinumwindow import PlatinumWindow
from games.heartsoul import HeartSoulWindow
from games.blackwhitewindow import BlackWhiteWindow
from games.black2white2window import Black2White2Window
from games.xandywindow import XAndYWindow
from games.omegaalphawindow import OmegaAlphaWindow
from games.sunmoonwindow import SunMoonWindow
from games.ultrawindow import UltraWindow
from games.swordshieldwindow import SwordShieldWindow
from games.crimsonvioletwindow import CrimsonVioletWindow


class ScoreGUI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nuzlocke Scorer")

        layout = QGridLayout()

        # Game select
        game_select_label = QLabel("Game Select:")

        self.game_select = QComboBox()

        self.game_select.addItems([
            'RB',
            'Yellow',
            'GSC',
            'Emerald',
            'FRLG',
            'DP',
            'Platinum',
            'HGSS',
            'BW',
            'B2W2',
            'XY',
            'ORAS',
            'SM',
            'USUM',
            'SwSh',
            'CV',
            "WaWi"
        ])

        layout.addWidget(game_select_label, 0, 0)
        layout.addWidget(self.game_select, 0, 1)

        # Button
        choose_button = QPushButton("Choose...")
        choose_button.clicked.connect(self.choose_game)

        layout.addWidget(choose_button, 1, 0)

        # Central widget
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        # Store open windows
        self.windows = []

        # Game -> Window class mapping
        self.game_windows = {
            'RB': RedBlueWindow,
            'Yellow': YellowWindow,
            'GSC': GoldSilverCrystalWindow,
            'RS': RubySapphireWindow,
            'Emerald': EmeraldWindow,
            'DP': DiamondPearlWindow,
            'Platinum': PlatinumWindow,
            'HGSS': HeartSoulWindow,
            'BW': BlackWhiteWindow,
            'B2W2': Black2White2Window,
            "XY": XAndYWindow,
            "ORAS": OmegaAlphaWindow,
            "SM": SunMoonWindow,
            "USUM": UltraWindow,
            "SwSh": SwordShieldWindow,
            "CV": CrimsonVioletWindow,
        }

    def choose_game(self):

        game = self.game_select.currentText()

        window_class = self.game_windows.get(game)

        if window_class is not None:

            window = window_class()

            self.windows.append(window)

            window.show()

        else:
            print(f"{game} not implemented yet")