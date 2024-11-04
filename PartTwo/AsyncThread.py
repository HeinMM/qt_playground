import sys
import time
import datetime
from random import randint
from PyQt6.QtCore import Qt, QRunnable, QThreadPool,pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QPushButton, QScrollArea, QVBoxLayout, QWidget, QLabel


class WorkerSignals(QObject):
    result_ready = pyqtSignal(int)



class Worker(QRunnable):
    def __init__(self, worker_id, signals):
        super().__init__()
        self.worker_id = worker_id
        self.signals = signals


    def run(self):
        time.sleep(1)
        result = self.worker_id * 10
        print(result)
        self.signals.result_ready.emit(result)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QRunable Example")
        self.setFixedSize(300,200)

        vbox = QVBoxLayout()
        self.button = QPushButton("Start")
        self.button.clicked.connect(self.start_tasks)

        vbox.addWidget(self.button)

        self.scroll_area = QScrollArea()
        self.results_label = QLabel("Results : ")
        self.results_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.results_label)

        vbox.addWidget(self.scroll_area)
        self.setLayout(vbox)


        self.thread_pool = QThreadPool()


    def start_tasks(self):
        self.button.setEnabled(False)



        for i in range(1,6):
            time.sleep(1)
            signals = WorkerSignals()
            worker = Worker(i, signals)
            signals.result_ready.connect(self.collect_result)
            self.thread_pool.start(worker)



    def collect_result(self, result):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_results = self.results_label.text()
        new_result = f"Worker Result : {result} at {current_time}"
        self.results_label.setText(current_results + "<br>" + new_result)

        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())


        if self.thread_pool.activeThreadCount() == 0:
            self.button.setEnabled(True)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())