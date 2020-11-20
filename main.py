import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from UI.mainUI import Ui_MainWindow_Main
from UI.addEditCoffeeForm import Ui_MainWindow


class addRed(QMainWindow, Ui_MainWindow):
    def __init__(self, p, red=False, index=None):
        super().__init__()
        self.setupUi(self)
        self.index = index
        self.p = p
        self.show()

        if red:
            self.setWindowTitle('Изменить')
            self.btn.setText('Изменить')
            self.btn.clicked.connect(self.red)
            self.load()
        else:
            self.btn.clicked.connect(self.add)

    def add(self):
        if self.lineSort.text():
            if self.lineRoast.text():
                if self.lineDesc.text():
                    if self.lineCost.text():
                        if self.lineSize.text():
                            try:
                                con = sqlite3.connect('data/coffee.sqlite')
                                cur = con.cursor()
                                cur.execute("""INSERT INTO 
                                coffee(sort, roast, ground, desription, cost, size) 
                                VALUES(?, ?, ?, ?, ?, ?)""", (self.lineSort.text(),
                                                              self.lineRoast.text(), self.comboBox.currentIndex(),
                                                              self.lineDesc.text(),
                                                              self.lineCost.text(), self.lineSize.text()))
                                con.commit()
                                self.p.loadData()
                            except Exception as e:
                                print(e)
        return

    def load(self):
        try:
            index = int(self.p.tbl.item(self.index, 0).text())
            con = sqlite3.connect('data/coffee.sqlite')
            cur = con.cursor()
            result = cur.execute("""SELECT * FROM coffee WHERE ID = ?""", (index,)).fetchone()

            self.lineSort.setText(result[1])
            self.lineRoast.setText(str(result[2]))
            self.comboBox.setCurrentIndex(result[3])
            self.lineDesc.setText(result[4])
            self.lineCost.setText(str(result[5]))
            self.lineSize.setText(str(result[6]))
        except Exception as e:
            print(e)

    def red(self):
        if self.lineSort.text():
            if self.lineRoast.text():
                if self.lineDesc.text():
                    if self.lineCost.text():
                        if self.lineSize.text():
                            try:
                                index = int(self.p.tbl.item(self.index, 0).text())
                                con = sqlite3.connect('data/coffee.sqlite')
                                cur = con.cursor()
                                cur.execute("""UPDATE coffee 
                                SET sort = ?, roast = ?,
                                ground = ?, desription = ?,
                                cost = ?, size = ?
                                WHERE ID = ?""", (self.lineSort.text(),
                                                  self.lineRoast.text(), self.comboBox.currentIndex(),
                                                  self.lineDesc.text(),
                                                  self.lineCost.text(), self.lineSize.text(),
                                                  index))
                                con.commit()
                                self.p.loadData()
                            except Exception as e:
                                print(e)
        return


class MyWidget(QMainWindow, Ui_MainWindow_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadData()
        self.index = None

        self.btnAdd.clicked.connect(self.add)
        self.btnRed.clicked.connect(self.red)
        self.tbl.itemClicked.connect(self.changeIndex)

    def changeIndex(self, index):
        self.index = index.row()

    def red(self):
        if self.index is not None:
            self.form = addRed(self, True, self.index)
            self.index = None

    def add(self):
        self.form = addRed(self)

    def loadData(self):
        con = sqlite3.connect('data/coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()

        self.tbl.setRowCount(len(result))
        for n, (_id, title, roast, ground, description, cost, size) in enumerate(result):
            self.tbl.setItem(n, 0, QTableWidgetItem(str(_id)))
            self.tbl.setItem(n, 1, QTableWidgetItem(str(title)))
            self.tbl.setItem(n, 2, QTableWidgetItem(str(roast)))
            if ground:
                self.tbl.setItem(n, 3, QTableWidgetItem('В зёрнах'))
            else:
                self.tbl.setItem(n, 3, QTableWidgetItem('Молотый'))
            self.tbl.setItem(n, 4, QTableWidgetItem(str(description)))
            self.tbl.setItem(n, 5, QTableWidgetItem(str(cost)))
            self.tbl.setItem(n, 6, QTableWidgetItem(str(size)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())