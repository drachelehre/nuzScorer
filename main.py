import sys
from PyQt6.QtWidgets import QApplication
from scoregui import *


def main():
    app = QApplication(sys.argv)
    window = ScoreGUI()

    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
