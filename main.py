import sys
import datetime
import sqlite3

from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QFontDatabase, QColor
from PyQt5.QtWidgets import *

class WidgetToDo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wrapper = QWidget(self)
        self.initUI()

    def initUI(self):
        self.resize(500, 500)
        self.setWindowTitle('PyToDo')
        self.statusBar().showMessage("Запущено")
        self.setWindowToCenter()

        self.vbox = QVBoxLayout(self.wrapper)
        self.h1box = QHBoxLayout(self.wrapper)

        self.table = QTableWidget(self)

        self.task_line = QLineEdit(self)
        self.task_line.setPlaceholderText("Введите текст задачи")
        self.task_line.textChanged.connect(self.enable_disable_button)

        self.task_date = QDateEdit(self)
        self.task_date.setCalendarPopup(True)

        self.task_btn = QPushButton(self)
        self.task_btn.setEnabled(False)
        self.task_btn.setText("Добавить")
        self.task_btn.clicked.connect(self.addTask)

        self.layout_sizePol_init()
        self.table_init()
        self.setCentralWidget(self.wrapper)
        self.getTodayDate()
        self.outputTaskTable()
        self.set_font()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetToDo()
    sys.exit(app.exec_())