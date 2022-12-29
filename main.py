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

    def layout_sizePol_init(self):
        self.vbox.setSpacing(10)
        self.vbox.addWidget(self.table)
        self.vbox.addLayout(self.h1box)
        self.h1box.addWidget(self.task_line)
        self.h1box.addWidget(self.task_date)
        self.h1box.addWidget(self.task_btn)
        self.h1box.addWidget(self.sort_btn)
        self.h1box.addWidget(self.sort_combo)
        #self.h1box.addWidget(self.sort_u_btn)
        self.setLayout(self.vbox)

        self.sizePolicy_task_date = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.sizePolicy_task_date.setHorizontalStretch(30)
        self.task_date.setSizePolicy(self.sizePolicy_task_date)

        self.sizePolicy_task_line = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.sizePolicy_task_line.setHorizontalStretch(100)
        self.task_line.setSizePolicy(self.sizePolicy_task_line)

    def enable_disable_button(self):
        if self.task_line.text():
            self.task_btn.setEnabled(True)
        else:
            self.task_btn.setEnabled(False)

    def table_init(self):
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Номер", "Задача", "Дата", "Статус"])

        #self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.verticalHeader().setVisible(False)

        self.table.cellDoubleClicked.connect(self.rowSelected)

        self.table.setRowCount(0)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Подтверждение',
                                     "Подтвердите выход", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetToDo()
    sys.exit(app.exec_())