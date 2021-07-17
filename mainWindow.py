# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 960)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lCMM_8 = QtWidgets.QLabel(self.centralwidget)
        self.lCMM_8.setObjectName("lCMM_8")
        self.gridLayout_4.addWidget(self.lCMM_8, 0, 0, 1, 1)
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setObjectName("input")
        self.gridLayout_4.addWidget(self.input, 0, 1, 1, 1)
        self.inputFind = QtWidgets.QPushButton(self.centralwidget)
        self.inputFind.setObjectName("inputFind")
        self.gridLayout_4.addWidget(self.inputFind, 0, 2, 1, 1)
        self.lCMM_3 = QtWidgets.QLabel(self.centralwidget)
        self.lCMM_3.setObjectName("lCMM_3")
        self.gridLayout_4.addWidget(self.lCMM_3, 1, 0, 1, 1)
        self.outputFind = QtWidgets.QPushButton(self.centralwidget)
        self.outputFind.setObjectName("outputFind")
        self.gridLayout_4.addWidget(self.outputFind, 1, 2, 1, 1)
        self.output = QtWidgets.QLineEdit(self.centralwidget)
        self.output.setObjectName("output")
        self.gridLayout_4.addWidget(self.output, 1, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setObjectName("convert")
        self.horizontalLayout_3.addWidget(self.convert)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_9.addWidget(self.line_2)
        self.verticalLayout.addLayout(self.verticalLayout_9)
        self.console = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.console.setFont(font)
        self.console.setReadOnly(True)
        self.console.setObjectName("console")
        self.verticalLayout.addWidget(self.console)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lCMM_8.setText(_translate("MainWindow", "Input Folder"))
        self.inputFind.setText(_translate("MainWindow", "..."))
        self.lCMM_3.setText(_translate("MainWindow", "Output Folder"))
        self.outputFind.setText(_translate("MainWindow", "..."))
        self.convert.setText(_translate("MainWindow", "Unpack"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

