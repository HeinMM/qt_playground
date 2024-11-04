import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QIcon, QColor, QPixmap
from PyQt6.QtCore import Qt


class EventLogTable(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the table widget
        self.table = QTableWidget()
        self.table.setColumnCount(7)  # Set the number of columns

        # Set headers with a calendar icon for the first header
        pixmap  = QPixmap("icons/calendar.png")  # Replace with your calendar icon path
        icon = QIcon(pixmap.scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        headers = ["", "State", "Date", "Subject", "UID", "Port", "Val"]

        # Add headers to the table
        for i, header in enumerate(headers):
            if i == 0:
                # Create an empty header item
                item = QTableWidgetItem()
                item.setIcon(icon)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setHorizontalHeaderItem(i, item)
            else:
                # Create header item with text
                item = QTableWidgetItem(header)
                item.setForeground(QColor("white"))  # Set text color to white
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Center-align text
                self.table.setHorizontalHeaderItem(i, item)

        # Set table properties
        self.table.horizontalHeader().setStretchLastSection(True)
        #self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)  # Fixed sizes for all columns
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # Make columns stretch
        self.table.verticalHeader().setVisible(False)  # Hide row numbers
        self.table.setAlternatingRowColors(False)
        self.table.setShowGrid(True)

        # Remove the vertical header lines by customizing the stylesheet
        self.table.setStyleSheet("""
                   QHeaderView::section {
                       background-color: #1F2024;
                       color: white;
                       padding: 1px;
                       border: none;  /* Remove the vertical header lines */
                       border-bottom: 1px solid white;  /* Add blue line at the bottom */
                       height: 35px;
                   }
                   QTableWidget {
                       padding: 0px;
                       margin: 0px;
                       background-color: #1F2024;
                       color: white;
                       gridline-color: #1F2024;
                       border: none;
                   }
               """)

        self.set_column_widths()

        # Set the layout and add the table
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

        # Fill the table with example rows (optional)
        self.fill_table_with_example_data()


    def set_column_widths(self):
        # Define the width proportions
        proportions = [0, 8, 12,12, 3, 3, 0]
        total_proportion = sum(proportions)

        # Calculate each column width based on the table width
        table_width = self.table.width()
        column_widths = [(table_width / total_proportion) * proportion for proportion in proportions]

        # Set each column width
        for i, width in enumerate(column_widths):
            self.table.setColumnWidth(i, int(width))



    def fill_table_with_example_data(self, icon=None):
        # Set some example data

        '''
        example_data = [
            ["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],
            ["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],
            ["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],
            ["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],
            ["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],
            ["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],
            ["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],
            ["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],
            ["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],
            ["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],["", "Active", "2024-11-04 12:12 pm monday", "System Check", "12345", "1", "Normal"],
            ["", "Inactive", "2024-11-03", "Update", "12346", "2", "Warning"],
            ["", "Active", "2024-11-02", "Backup", "12347", "3", "Error"]
        ]
        '''


        example_data = []

        self.table.setRowCount(len(example_data))  # Set the row count

        for row, data in enumerate(example_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(value)
                if col == 0 and icon:  # Add icon to the first column
                    item.setIcon(icon)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(row, col, item)



