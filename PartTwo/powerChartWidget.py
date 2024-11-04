import sys
from cProfile import label

from global_color.colors import GlobalColor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap, QPainter, QColor, QFont, QIcon
from PyQt6.QtCore import Qt, QSize
import warnings

class PowerChartWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the Matplotlib figure and axis
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.figure.patch.set_facecolor(GlobalColor.FOOTER_BACKGROUND)
        self.canvas = FigureCanvas(self.figure)



        # Generate the plot
        self.plot_voltage_chart()

        # Set layout and add the Matplotlib canvas
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        #self.setStyleSheet("background-color: black;")

    def plot_voltage_chart(self):
        # Voltage data and labels
        voltages = [29.07, 22.06, 22.08]
        labels = ["A-B", "B-C", "C-A"]
        y_pos = np.arange(len(labels))

        # Create a horizontal bar chart
        self.ax.barh(y_pos, voltages, color=GlobalColor.STATUS_ON, height=0.45, align="center")

        # Add data labels next to each bar
        for i, v in enumerate(voltages):
            self.ax.text(v + 5, i, f"{v:.2f}", va='center', color=GlobalColor.WHITE, fontsize=8)

        # Customize the appearance
        self.ax.set_yticks(y_pos)
        self.ax.set_yticklabels(labels, color="white")
        self.ax.set_title("CURRENT", color=GlobalColor.TEXT_COLOR, fontsize=8, pad=13)
        self.ax.set_xlim(0, 600)
        self.ax.set_facecolor(GlobalColor.FOOTER_BACKGROUND)
        self.ax.spines['top'].set_color(GlobalColor.STATUS_OFF)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_color(GlobalColor.STATUS_OFF)
        self.ax.spines['bottom'].set_color(GlobalColor.STATUS_OFF)
        self.ax.tick_params(axis='x', colors=GlobalColor.STATUS_OFF, labelsize = 8)
        self.ax.tick_params(axis='y', colors=GlobalColor.STATUS_OFF, labelsize = 8)

        #self.ax.text(225, -1.2, "Voltage", color="white", fontsize=8, ha='center')

        # Set only 342 and 418 as x-axis ticks
        self.ax.set_xticks([350])
        self.ax.set_xticklabels(["350"], color="yellow")
        self.ax.spines['bottom'].set_color(GlobalColor.STATUS_OFF)  # Show bottom spine in white
        self.ax.tick_params(axis='x', colors=GlobalColor.WHITE)  # X-axis tick colors set to white

        # Add red dashed lines for target voltages
        target = 342
        self.ax.axvline(target, color=GlobalColor.RED, linestyle="--")


        self.ax.hlines(0.5,xmin=0, xmax=600, colors=GlobalColor.STATUS_OFF, linestyles="solid", linewidth=1)
        self.ax.hlines(1.5, xmin=0, xmax=600, colors=GlobalColor.STATUS_OFF, linestyles="solid", linewidth=1)

        custom_ticks = [1, 5, 9, 13, 17, 21, 25, 29, 33]


        # Update the canvas to reflect the changes
        self.canvas.draw()


