# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout.addWidget(self.btnAdd, 1, 0, 1, 1)
        self.btnRed = QtWidgets.QPushButton(self.centralwidget)
        self.btnRed.setObjectName("btnRed")
        self.gridLayout.addWidget(self.btnRed, 1, 1, 1, 1)
        self.tbl = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl.setObjectName("tbl")
        self.tbl.setColumnCount(7)
        self.tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tbl, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 469, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Эспрессо"))
        self.btnAdd.setText(_translate("MainWindow", "Добавить"))
        self.btnRed.setText(_translate("MainWindow", "Изменить"))
        item = self.tbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "название сорта"))
        item = self.tbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "степень обжарки"))
        item = self.tbl.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "молотый/в зёрнах"))
        item = self.tbl.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "описание вкуса"))
        item = self.tbl.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "цена"))
        item = self.tbl.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "объём упаковки"))