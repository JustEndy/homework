import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        self.loadData()

    def loadData(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()

        self.tbl.setRowCount(len(result))
        for n, (_id, title, roast, ground, description, cost, size) in enumerate(result):
            self.tbl.setItem(n, 0, QTableWidgetItem(str(_id)))
            self.tbl.setItem(n, 1, QTableWidgetItem(str(title)))
            self.tbl.setItem(n, 2, QTableWidgetItem(str(roast)))
            self.tbl.setItem(n, 3, QTableWidgetItem(str(ground)))
            self.tbl.setItem(n, 4, QTableWidgetItem(str(description)))
            self.tbl.setItem(n, 5, QTableWidgetItem(str(cost)))
            self.tbl.setItem(n, 6, QTableWidgetItem(str(size)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())