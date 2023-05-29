from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from .extras.flowLayout import FlowLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignLeft)

        cars: list[str] = ["hatchback", "off-road", "sedan"]
        for car in cars:
            icon = QIcon(QPixmap(f"/home/redmi/Code/db_qt/src/resource/images/cars/{car}"))
            button = QPushButton(car)
            button.setIcon(icon)
            button.setIconSize(QSize(32, 32))
            button.setObjectName(f"button_{car}")
            button.clicked.connect(self.on_button_clicked)
            v_layout.addWidget(button)

        # v_layout.setStretch(0, 1)
        self.setLayout(v_layout)
        self.setWindowTitle("Mark I")
        self.setWindowIcon(QIcon("/home/redmi/Code/db_qt/src/resource/images/icon/icon.png"))
        self.resize(700, 500)

        v_layout2 = QVBoxLayout()
        v_layout2.setAlignment(Qt.AlignCenter)
        self.setLayout(v_layout2)
        v_layout2.addWidget(FlowLayout())


    def on_button_clicked(self):
        sender = self.sender()
        button_id = sender.objectName()

        if button_id == "button_sedan":
            print("TEST")
            ...
