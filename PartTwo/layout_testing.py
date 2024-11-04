import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QVBoxLayout, QLabel, QFrame, QHBoxLayout
)
from PyQt6.QtCore import Qt

from PartTwo.EventLogTableWidget import EventLogTable
from PartTwo.Power_Card_Widget import PowerCardWidget
from PartTwo.Status_Card_Witget import StatusCardWidget
from PartTwo.VoltageChartWidget import VoltageChartWidget
from PartTwo.currentChartWidget import CurrentChartWidget
from PartTwo.global_color.colors import GlobalColor


class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        # Sample Cards
        self.voltage_card(layout, 0, 0)
        self.current_card(layout, "Current", "Sample current data", 0, 1)
        self.power_card(layout,  0, 2)
        self.status_card(layout, 1, 0)
        self.create_card(layout, "EVENT LOG2", 1, 1, 1, 2)

        self.setLayout(layout)
        self.setWindowTitle("Dashboard Layout")
        self.resize(1024, 600)

    def voltage_card(self, layout, row, col, row_span=1, col_span=1):
        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setStyleSheet(f"background-color: {GlobalColor.BACKGROUND}; color: white; padding: 10px;")

        card_layout = QVBoxLayout()

        ab = 387.97
        bc = 386.58
        ca = 387.62

        voltage_chart = VoltageChartWidget(ab,bc,ca)
        card_layout.addWidget(voltage_chart, alignment=Qt.AlignmentFlag.AlignCenter)

        card.setLayout(card_layout)
        layout.addWidget(card, row, col, row_span, col_span)

    def current_card(self, layout, title, content, row, col, row_span=1, col_span=1):
        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setStyleSheet(f"background-color: {GlobalColor.BACKGROUND}; color: white; padding: 10px;")

        card_layout = QVBoxLayout()

        a = 29.07
        b = 22.06
        c = 22.08

        current_chart = CurrentChartWidget(a,b,c)
        card_layout.addWidget(current_chart, alignment=Qt.AlignmentFlag.AlignCenter)

        card.setLayout(card_layout)
        layout.addWidget(card, row, col, row_span, col_span)

    def power_card(self, layout, row, col, row_span=1, col_span=1):

        active_power = 8175
        power_factor = 100
        frequency = 60

        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setStyleSheet(f"background-color: {GlobalColor.BACKGROUND}; color: white; padding-left: 90px; padding-right: 90px;")

        card_layout = QVBoxLayout()

        voltage_chart = PowerCardWidget(active_power,power_factor,frequency)
        card_layout.addWidget(voltage_chart, alignment=Qt.AlignmentFlag.AlignTop)

        card.setLayout(card_layout)
        layout.addWidget(card, row, col, row_span, col_span)

    def status_card(self, layout, row, col, row_span=1, col_span=1):
        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setStyleSheet(f"background-color: {GlobalColor.BACKGROUND}; color: white; padding: 90px;")

        signal_value = 3

        status_widget  = StatusCardWidget(signal_value)
        card_layout = QVBoxLayout()
        card_layout.addWidget(status_widget)
        card.setLayout(card_layout)
        layout.addWidget(card, row, col, row_span, col_span)

    def create_card(self, layout, title, row, col, row_span=1, col_span=1):
        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setStyleSheet(f"background-color: {GlobalColor.BACKGROUND}; padding: 0px; margin: 0px")

        card_layout = QVBoxLayout()


        title_label = QLabel(title)
        title_label.setStyleSheet(f'color:{GlobalColor.TEXT_COLOR}; font: 11px; padding: 5px;')
        card_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)

        event_table = EventLogTable()
        card_layout.addWidget(event_table)

        card.setLayout(card_layout)
        layout.addWidget(card, row, col, row_span, col_span)


app = QApplication(sys.argv)
window = DashboardWidget()
window.show()
sys.exit(app.exec())
