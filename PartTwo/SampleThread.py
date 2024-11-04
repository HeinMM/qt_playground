import sys
from PyQt6.QtCore import QThread, pyqtSignal
import time
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel

class WorkerThread(QThread):
    progress_updated = pyqtSignal(int)

    def run(self):
        for i in range(101):
            time.sleep(0.1)
            self.progress_updated.emit(i)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QThread Sample Example")
        self.setFixedSize(400,300)

        vbox = QVBoxLayout()
        self.button = QPushButton("Start")
        self.button.clicked.connect(self.start_thread)

        vbox.addWidget(self.button)

        self.progress_label = QLabel("Progress : ")
        vbox.addWidget(self.progress_label)

        self.setLayout(vbox)

        self.worker_thread = WorkerThread()
        self.worker_thread.progress_updated.connect(self.update_value)

    def start_thread(self):
        self.button.setEnabled(False)
        self.worker_thread.start()

    def update_value(self,value):
        self.progress_label.setText(f"Progress : {value}%")
        if value == 100:
            self.button.setEnabled(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())