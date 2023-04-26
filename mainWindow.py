import sys

from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QFileDialog, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from utils import read_data, pan_tompkins


class Window(QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure_1 = plt.figure(num=1)
        self.canvas_1 = FigureCanvas(self.figure_1)
        self.toolbar_1 = NavigationToolbar(self.canvas_1, self)

        # self.figure_2 = plt.figure(num=2)
        # self.canvas_2 = FigureCanvas(self.figure_2)
        # self.toolbar_2 = NavigationToolbar(self.canvas_2, self)
        #
        # self.figure_3 = plt.figure(num=3)
        # self.canvas_3 = FigureCanvas(self.figure_3)
        # self.toolbar_3 = NavigationToolbar(self.canvas_3, self)

        self.button = QPushButton('Загрузить данные')
        self.button.clicked.connect(self.plot)

        layout = QVBoxLayout()

        layout.addWidget(self.toolbar_1)
        layout.addWidget(self.canvas_1)

        # layout.addWidget(self.toolbar_2)
        # layout.addWidget(self.canvas_2)
        #
        # layout.addWidget(self.toolbar_3)
        # layout.addWidget(self.canvas_3)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def plot(self):
        wb_patch = QFileDialog.getOpenFileName()[0]
        eeg = read_data(wb_patch)
        peak_locs = pan_tompkins(eeg, 5000)

        self.figure_1.clear()
        # self.figure_2.clear()
        # self.figure_3.clear()

        ax_1 = self.figure_1.add_subplot(111)
        # ax_2 = self.figure_2.add_subplot()
        # ax_3 = self.figure_3.add_subplot()

        ax_1.plot(eeg)
        ax_1.scatter(peak_locs, eeg[peak_locs], c='r', marker='o')
        # ax_2.plot(filter_function_emg)
        # ax_3.plot(function_emg)
        # ax_3.plot(filter_function_emg)

        self.canvas_1.draw()
        # self.canvas_2.draw()
        # self.canvas_3.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
