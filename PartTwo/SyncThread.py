import sys
import time
import datetime
from random import randint
from turtledemo.penrose import start

from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QPushButton, QScrollArea, QVBoxLayout, QWidget, QLabel

class Worker(QThread):

    result_ready = pyqtSignal(int)

    def __init__(self, worker_id):
        super().__init__()
        self.worker_id = worker_id

    def run(self):
        time.sleep(randint(1,4))
        result = self.worker_id * 10
        print(result)
        self.result_ready.emit(result)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sync Example")
        self.setFixedSize(400,300)

        vbox = QVBoxLayout()
        self.button = QPushButton("Start")
        self.button.clicked.connect(self.start_tasks)

        vbox.addWidget(self.button)

        self.scrol_area = QScrollArea()
        self.result_label = QLabel("Results : ")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scrol_area.setWidgetResizable(True)
        self.scrol_area.setWidget(self.result_label)

        vbox.addWidget(self.scrol_area)
        self.setLayout(vbox)

        self.worker_threads = []

    def start_tasks(self):
        self.button.setEnabled(False)

        for i in range(1,7):
            time.sleep(1)
            worker = Worker(i)
            worker.result_ready.connect(self.collect_result)
            self.worker_threads.append(worker)
            worker.start()

    def collect_result(self, result):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_results = self.result_label.text()
        new_result = f"Worker Result: {result} at {current_time}"
        self.result_label.setText(current_results + "\n" + new_result)

        if len(self.worker_threads) == len([t for t in self.worker_threads if not t.isRunning()]):
            self.button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())