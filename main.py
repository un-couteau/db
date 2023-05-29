import sys

from PySide6.QtWidgets import QApplication

from src.frontend.ui.gui import Window


def main() -> None:
    app = QApplication(sys.argv)
    main_win = Window()
    main_win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
