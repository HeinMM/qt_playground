
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt, QSize

from PartTwo.global_color.colors import GlobalColor


class PowerCardWidget(QWidget):
    def __init__(self,active_power,power_factor,frequency):
        super().__init__()

        self.active_power = active_power
        self.power_factor = power_factor
        self.frequency = frequency

        self.signal_data_showing()


    def signal_data_showing(self):
        card_layout = QVBoxLayout()
        card_layout.setSpacing(0)
        card_layout.setContentsMargins(0, 0, 0, 0)

        title_label = QLabel("POWER")
        title_label.setStyleSheet(f'color:{GlobalColor.TEXT_COLOR}; padding:20px; font: 11px;')
        card_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel(f"{self.active_power} KW")
        title_label.setStyleSheet(f'color:{GlobalColor.WHITE}; padding:20px; font: 15px;')
        card_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel(f"{self.power_factor} %")
        title_label.setStyleSheet(f'color:{GlobalColor.WHITE}; padding:20px; font: 15px;')
        card_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel(f"{self.frequency} Hz")
        title_label.setStyleSheet(f'color:{GlobalColor.WHITE}; padding:20px; font: 15px;')
        card_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)



        self.setLayout(card_layout)

    def createCheckIcon(self):
        label = QLabel()
        pixmap = QPixmap("icons/green-circle.png")  # Replace with the path to your check icon image
        label.setPixmap(
            pixmap.scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        label.setStyleSheet("padding: 0px; margin: 0px;")
        return label




