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

from matplotlib.pyplot import margins

warnings.filterwarnings("ignore", category=DeprecationWarning)


class GraphWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setStyleSheet(f"background-color: {GlobalColor.BACKGROUND}; border: none; margin: 0px; padding: 0px;")
        # Create a Matplotlib figure and axis
        self.figure, (self.ax_current, self.ax_status) = plt.subplots(
            2, 1, gridspec_kw={'height_ratios': [10, 1]}, facecolor=GlobalColor.BACKGROUND
        )
        self.canvas = FigureCanvas(self.figure)

        # Use vertical layout to embed the canvas into the widget
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0,0,0,0)
        vLayout.setSpacing(0)
        vLayout.addWidget(self.canvas, stretch=10 )

        x_data = np.arange(1, 37)  # X-axis data (e.g., days or steps)
        y_data = np.random.randint(0, 65, size=36)  # Random Y-axis data (range up to 50)

        self.current_graph(x_data, y_data)
        plt.subplots_adjust(hspace=0.5)
        self.add_separator_line([0.25, 0.25])
        self.create_status_graph(y_data)
        self.add_separator_line([0.01, 0.01])
        # Add a legend below the STATUS graph

        #vLayout.addStretch()

        # Create and style the QLabel
        label_layout = QVBoxLayout()
        self.lable_id = QLabel("PM36 ID")
        self.lable_id.setStyleSheet(f"color: {GlobalColor.TEXT_COLOR}; font-size: 16px; ")
        #self.lable_id.setContentsMargins(50,0,0,0)
        self.lable_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the label to the layout
        #vLayout.addWidget(self.lable_id,alignment=Qt.AlignmentFlag.AlignCenter)
        #vLayout.setSpacing(10)
        icon_box = self.createIconBox()

        label_layout.addWidget(self.lable_id, alignment=Qt.AlignmentFlag.AlignCenter)
        label_layout.setSpacing(10)
        label_layout.addWidget(icon_box, alignment=Qt.AlignmentFlag.AlignCenter)
        label_layout.setContentsMargins(40,0,0,30)


        #vLayout.addWidget(icon_box,alignment=Qt.AlignmentFlag.AlignCenter)
        vLayout.addLayout(label_layout)
        self.setLayout(vLayout)


    def current_graph(self,x_data,y_data):
        # Example data (mimicking your graph)


        # Plot green bars
        bars = self.ax_current.bar(x_data, y_data, color='green', alpha=1 , zorder=2)

        # Add markers (triangle and square) on top of each bar
        for i, bar in enumerate(bars):
            height = bar.get_height()

            # Plot white square marker ('s') at the same position
            self.ax_current.plot(bar.get_x() + bar.get_width() / 2, height,
                         marker='s', markersize=3, color='white', markerfacecolor='white' , zorder=3)

            # Plot blue downward-pointing triangle marker ('v')
            self.ax_current.plot(bar.get_x() + bar.get_width() / 2, height + 0.5,
                         marker='v', markersize=4, color='blue', markerfacecolor='blue', zorder=3)

        # Set specific X-axis ticks to [1, 5, 9, ..., 33]
        custom_ticks = [1, 5, 9, 13, 17, 21, 25, 29, 33]
        self.ax_current.set_xticks(custom_ticks)  # Display only specific ticks

        self.ax_current.tick_params(axis='x', labelbottom=True)

        # Set Y-axis ticks at intervals of 5
        self.ax_current.set_yticks(np.arange(0, 70, 5))  # Y-axis ticks from 0 to 65


        # Add a red dashed threshold line at y=40
        self.ax_current.axhline(y=40, color=GlobalColor.RED, linestyle='--', linewidth=1, zorder=2)

        self.ax_current.spines['top'].set_visible(False)  # Disable top border
        self.ax_current.spines['right'].set_visible(False)  # Disable right border

        # Set border (spine) color to white
        for spine in ['left', 'bottom']:
            self.ax_current.spines[spine].set_edgecolor(GlobalColor.TEXT_COLOR)
            self.ax_current.spines[spine].set_linewidth(0.5)

        self.ax_current.grid(axis='y', color=GlobalColor.STATUS_OFF, linestyle='-', linewidth=0.5, zorder=1)
        self.ax_current.set_axisbelow(True)


        self.ax_current.set_facecolor(GlobalColor.FOOTER_BACKGROUND)
        self.ax_current.tick_params(colors=GlobalColor.TEXT_COLOR, labelsize = 7)

        # Set graph title and labels
        self.ax_current.set_title("CURRENT", color=GlobalColor.TEXT_COLOR, pad = 20)



        # Redraw the canvas to reflect the changes
        self.canvas.draw()

    def create_status_graph(self,y_data):
        """Function to create the STATUS graph based on current_graph's y_data values."""
        x = np.arange(1, 37)  # X-axis values matching current_graph x values

        # Define status colors based on y_data from current_graph
        colors = []
        for value in y_data:
            if value == 0:
                colors.append('gray')  # OFF
            elif value < 40:
                colors.append(GlobalColor.STATUS_ON)  # ON (under threshold)
            else:
                colors.append(GlobalColor.STATUS_TRIP)  # TRIP (above threshold)

        self.ax_status.clear()
        self.ax_status.bar(x, np.ones_like(x), color=colors, width=0.8)

        # Customize STATUS graph appearance
        self.ax_status.set_facecolor(GlobalColor.FOOTER_BACKGROUND)
        self.ax_status.tick_params(colors=GlobalColor.TEXT_COLOR)
        self.ax_status.set_yticks([])  # Hide y-axis ticks
        self.ax_status.set_title("STATUS", color=GlobalColor.TEXT_COLOR, pad=20)

        # Update X-ticks for status
        custom_ticks = list(range(1, 37))
        self.ax_status.set_xticks(custom_ticks)

        # Add legend texts under the STATUS graph
        self.ax_status.text(0.45, -1, '■', color='green', fontsize=14, ha='center', va='center',
                            transform=self.ax_status.transAxes)
        self.ax_status.text(0.47, -1.1, 'ON', color=GlobalColor.TEXT_COLOR, fontsize=12, ha='center', va='center',
                            transform=self.ax_status.transAxes)
        self.ax_status.text(0.49, -1, '■', color='gray', fontsize=14, ha='center', va='center',
                            transform=self.ax_status.transAxes)
        self.ax_status.text(0.511, -1.1, 'OFF', color=GlobalColor.TEXT_COLOR, fontsize=12, ha='center', va='center',
                            transform=self.ax_status.transAxes)
        self.ax_status.text(0.53, -1, '■', color=GlobalColor.STATUS_TRIP, fontsize=14, ha='center', va='center',
                            transform=self.ax_status.transAxes)
        self.ax_status.text(0.551, -1.1, 'TRIP', color=GlobalColor.TEXT_COLOR, fontsize=12, ha='center', va='center',
                            transform=self.ax_status.transAxes)

        # Set border styling for the status graph
        self.ax_status.spines['top'].set_visible(False)
        self.ax_status.spines['right'].set_visible(False)
        for spine in ['left', 'bottom']:
            self.ax_status.spines[spine].set_edgecolor(GlobalColor.TEXT_COLOR)
            self.ax_status.spines[spine].set_linewidth(0.5)

        # Adjust y-limits to ensure the text is visible and redraw
        self.ax_status.set_ylim(-1, 1.5)
        self.canvas.draw()



    def add_legend(self):
        """Create a horizontal legend for the status graph."""
        legend_widget = QWidget()
        legend_layout = QHBoxLayout()
        legend_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for compact layout
        legend_layout.setSpacing(10)  # Adjust spacing between legend items

        # Create labels for each legend entry
        on_label = QLabel('■ ON')
        on_label.setStyleSheet('color: green; font-weight: bold;')

        off_label = QLabel('■ OFF')
        off_label.setStyleSheet('color: gray; font-weight: bold;')

        trip_label = QLabel('■ TRIP')
        trip_label.setStyleSheet(f'color: {GlobalColor.STATUS_TRIP}; font-weight: bold;')

        # Add labels to the layout
        legend_layout.addWidget(on_label)
        legend_layout.addWidget(off_label)
        legend_layout.addWidget(trip_label)

        #legend_layout.addStretch()  # Push the items to the left

        legend_widget.setLayout(legend_layout)
        return legend_widget

    def add_separator_line(self,y_position):
        """Draw a black horizontal line between the two graphs."""
        # Use the figure's coordinates to add a line across the figure
        self.figure.subplots_adjust(hspace=0.6)  # Adjust space between graphs

        # Draw a black line across the figure between the two graphs
        #line = plt.Line2D([0.1, 0.91], [0.25, 0.25], color='#1C1D21', linewidth=2, transform=self.figure.transFigure)
        #line = plt.Line2D([0.1, 0.91], [0.01, 0.01], color='red', linewidth=2, transform=self.figure.transFigure)
        line = plt.Line2D([0.1, 0.91], y_position, color='#1C1D21', linewidth=2, transform=self.figure.transFigure)
        self.figure.add_artist(line)

    def createIconBox(self):
        # Create a widget to act as the container for the icon and number
        icon_widget = QWidget()
        icon_widget.setFixedSize(60, 60)  # Set the size of the box

        icon_widget.setStyleSheet("background-color: #19481E; border-radius: 5px;")  # Box color and style


        # Create an inner layout for the icon and number
        icon_layout = QHBoxLayout()
        icon_layout.setContentsMargins(0, 0, 0, 0)  # Adjust margins for padding
        icon_layout.setSpacing(10)  # Space between icon and number

        # Create the green check icon (using QPixmap or custom painting)
        check_label = QLabel()
        check_icon = self.createCheckIcon()
        check_label.setPixmap(check_icon)
        icon_layout.addWidget(check_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create the number label
        number_label = QLabel("1")
        number_label.setStyleSheet("color: white; font-size: 20px;")
        icon_layout.addWidget(number_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Align the layout within the box
        icon_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


        icon_widget.setLayout(icon_layout)

        return icon_widget

    def createCheckIcon(self):
        """Create a green circular check icon using QPixmap."""
        pixmap = QPixmap(QSize(20, 20))  # Size of the icon
        pixmap.fill(Qt.GlobalColor.transparent)  # Make the background transparent

        # Draw the green check mark inside the pixmap
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor("#00FF00"))  # Green color
        painter.setPen(Qt.PenStyle.NoPen)  # No border for the circle
        painter.drawEllipse(0, 0, 20, 20)  # Draw the green circle
        painter.end()

        return pixmap





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Graph Example')

        # Create the header
        header = self.create_header()

        # Initialize and set the graph widget as the central widget
        graph_widget = GraphWidget()
        # Create footer
        footer = self.create_footer()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(header)
        main_layout.addWidget(graph_widget)
        main_layout.setSpacing(60)
        main_layout.addWidget(footer)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setStyleSheet(f"background-color: {GlobalColor.FOOTER_BACKGROUND};")
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.showFullScreen()

    def create_header(self):
        """Create the header section with reduced height."""
        header = QWidget()
        header.setStyleSheet(f"background-color: {GlobalColor.HEADER_BACKGROUND};")

        # Set a fixed height for the header
        header.setFixedHeight(50)  # Adjust height as needed

        # Create header layout
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 10, 0)  # Reduce margins
        layout.setSpacing(10)  # Reduce spacing between widgets

        # Add a title to the header
        title = QLabel("NAVER")
        title.setStyleSheet(f"color: {GlobalColor.ACTIVE_TEXT_COLOR}; font-size: 25px; font-weight: bold;")
        layout.addWidget(title)

        # Add an Exit button
        exit_button = QPushButton("LOGOUT")
        exit_button.setStyleSheet("color: white; background-color: red; font-weight: bold;")
        exit_button.setFixedSize(60, 30)  # Adjust button size
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        # Set the layout for the header widget
        header.setLayout(layout)
        return header

    def keyPressEvent(self, event):
        """Exit full-screen mode when 'Esc' is pressed."""
        if event.key() == Qt.Key.Key_Escape:
            self.showNormal()  # Exit full screen and return to normal window

    def create_footer(self):
        footer = QWidget()
        footer.setFixedHeight(100)  # Set height for footer
        footer.setStyleSheet(f"background-color: {GlobalColor.FOOTER_BACKGROUND}; border-top: 2px solid {GlobalColor.HEADER_BACKGROUND};")  # Dark background

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Margin on left and right
        layout.setSpacing(50)  # Space between items

        # Create left and right spacers
        left_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        right_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        layout.addItem(left_spacer)
        # Add footer icons and labels
        dashboard_button = self.create_footer_button("DASHBOARD", "icons/home.png")
        detail_button = self.create_footer_button("DETAIL", "icons/details.png")
        settings_button = self.create_footer_button("SETTING", "icons/setting.png")


        # Add buttons to layout
        layout.addWidget(dashboard_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(detail_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(settings_button, alignment=Qt.AlignmentFlag.AlignCenter)



        layout.addItem(right_spacer)

        footer.setLayout(layout)
        return footer

    def create_footer_button(self, text, icon_path):
        # Create a QWidget to hold the icon and text vertically
        button_widget = QWidget()
        button_widget.setContentsMargins(5,5,5,5)
        button_layout = QVBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(2)  # Adjust spacing between icon and text

        # Create the icon as a QLabel and set an icon pixmap
        icon_label = QLabel()
        icon_label.setPixmap(QIcon(icon_path).pixmap(QSize(40, 40)))  # Adjust icon size as needed
        icon_label.setStyleSheet("background-color: rgba(0, 0, 0, 0);border: none;")
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create the text label for the button
        text_label = QLabel(text)
        text_label.setStyleSheet(f"background-color: rgba(0, 0, 0, 0); color: {GlobalColor.TEXT_COLOR}; font-size: 16px; border:none")
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the icon and text to the layout
        button_layout.addWidget(icon_label)
        button_layout.addWidget(text_label)

        button_widget.setStyleSheet(f"""
            QWidget {{
            background-color: rgba(0, 0, 0, 0);
            border: none;
        }}
        QWidget:hover {{
            background-color: {GlobalColor.BUTTON_HOVER_BACKGROUND};  /* Hover color */
        }}
        QWidget:hover QLabel {{
            color: red;  /* Hover color */
        }}
        """)

        # Set the layout to the QWidget
        button_widget.setLayout(button_layout)

        return button_widget



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
