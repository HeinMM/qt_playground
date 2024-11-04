from signal import signal

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt, QSize

from PartTwo.global_color.colors import GlobalColor


class StatusCardWidget(QWidget):
    def __init__(self,signal_value):
        super().__init__()
        self.signal_value = signal_value
        self.signal_data_showing()


    def signal_data_showing(self):
        card_layout = QVBoxLayout()
        card_layout.setSpacing(0)
        card_layout.setContentsMargins(0, 0, 0, 0)

        title_label = QLabel("STATUS")
        title_label.setStyleSheet(f'color:{GlobalColor.TEXT_COLOR}; padding:20px; font: 11px;')
        card_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)
        #if (self.signal_value == 1 | | self.signal_value == 3):
        if self.signal_value == 1 or self.signal_value ==3:
            signal_one_layout = QHBoxLayout()
            icon_one = self.createCheckIcon()
            signal_one = QLabel("TRIP")
            signal_one.setStyleSheet(f'color:{GlobalColor.WHITE}; padding:0px; font: 15px; margin:0px;')
            signal_one_layout.addWidget(icon_one, alignment=Qt.AlignmentFlag.AlignCenter)
            signal_one_layout.addWidget(signal_one)
            signal_one_layout.setContentsMargins(0, 0, 0, 0)  # Remove extra margins
            signal_one_layout.setSpacing(0)
            card_layout.addLayout(signal_one_layout)

        if self.signal_value == 2 or self.signal_value == 3:
            signal_two_layout = QHBoxLayout()
            icon_two = self.createCheckIcon()
            signal_two = QLabel("COMM")
            signal_two.setStyleSheet(f'color:{GlobalColor.WHITE}; padding:0px; font: 15px; margin:0px;')
            signal_two_layout.addWidget(icon_two, alignment=Qt.AlignmentFlag.AlignCenter)
            signal_two_layout.addWidget(signal_two)
            signal_two_layout.setContentsMargins(0, 0, 0, 0)  # Remove extra margins
            signal_two_layout.setSpacing(0)
            card_layout.addLayout(signal_two_layout)



        self.setLayout(card_layout)

    def createCheckIcon(self):
        label = QLabel()
        pixmap = QPixmap("icons/green-circle.png")  # Replace with the path to your check icon image
        label.setPixmap(
            pixmap.scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        label.setStyleSheet("padding: 0px; margin: 0px;")
        return label




