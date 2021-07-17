# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 12:39:02 2021

@author: AsteriskAmpersand
"""

import sys
import os
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from mainWindow import Ui_MainWindow
import arcUnpack as ARC
from pathlib import Path

def checkPath(path):
    return os.path.isdir(path)

STORIESTITLE = r""" _  _   __   __ _  ____  ____  ____  ____    _  _  _  _  __ _  ____  ____  ____    ____  ____  __  ____  __  ____  ____    ____ 
( \/ ) /  \ (  ( \/ ___)(_  _)(  __)(  _ \  / )( \/ )( \(  ( \(_  _)(  __)(  _ \  / ___)(_  _)/  \(  _ \(  )(  __)/ ___)  (___ \
/ \/ \(  O )/    /\___ \  )(   ) _)  )   /  ) __ () \/ (/    /  )(   ) _)  )   /  \___ \  )( (  O ))   / )(  ) _) \___ \   / __/
\_)(_/ \__/ \_)__)(____/ (__) (____)(__\_)  \_)(_/\____/\_)__) (__) (____)(__\_)  (____/ (__) \__/(__\_)(__)(____)(____/  (____)"""

TOOLTITLE =  r""" _  _  __ _  ____   __    ___  __ _  ____  ____    ____  __    __   __   
/ )( \(  ( \(  _ \ / _\  / __)(  / )(  __)(  _ \  (_  _)/  \  /  \ (  )  
) \/ (/    / ) __//    \( (__  )  (  ) _)  )   /    )( (  O )(  O )/ (_/\
\____/\_)__)(__)  \_/\_/ \___)(__\_)(____)(__\_)   (__) \__/  \__/ \____/"""
SPACE = "=========================================================================================================================="

def outputWindow(console):
    def output(x):
        console.append(" "*4+str(x))
        QtWidgets.QApplication.processEvents()
    return output

class progressBarProcessor():
    def __init__(self,pbar):
        self.pbar = pbar
    def setValue(self,x):
        self.pbar.setValue(x)
        QtWidgets.QApplication.processEvents() 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, arguments):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Monster Hunter Stories 2 Unpacker Tool")
        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        elif __file__:
            application_path = os.path.dirname(__file__)
        self.setWindowIcon(QtGui.QIcon(application_path+r"\resources\DodoSama.png"))
        self.connect()
        self.show()
        self.ui.progressBar.setValue(0)
        self.ui.console.append(STORIESTITLE)
        self.ui.console.append("")
        self.ui.console.append(TOOLTITLE)
        self.ui.console.append("")
        self.ui.console.append("==========================================================================================================================")
        self.ui.console.append("Written by Silvris, UI and Packaging by Asterisk")
        self.ui.console.append("Silvris: https://github.com/Silvris")
        self.ui.console.append("Asterisk: https://github.com/AsteriskAmpersand")
        self.ui.console.append("")
        self.ui.console.append("This is a free tool, if you paid for it, you've been scammed") 
        self.ui.console.append("==========================================================================================================================")
    def pathCheck(self,output):
        if not checkPath(self.ui.input.text()):
            output("Input Folder %s does not exist."%self.ui.input.text())
            return False
        if not self.ui.output.text():
            output("No Output Folder specified.")
            return False
        return True
    
    def execute(self):
        self.ui.progressBar.setValue(0)
        output = outputWindow(self.ui.console)
        if not self.pathCheck(output):
            return
        self.ui.console.append("Starting Extraction:")
        pbar = progressBarProcessor(self.ui.progressBar)
        ARC.extractChunk(self.ui.input.text(),self.ui.output.text(),output,pbar)
        self.ui.console.append(SPACE)
    def connect(self):
        self.ui.convert.clicked.connect(self.execute)
        self.ui.inputFind.clicked.connect(self.getInput)
        self.ui.outputFind.clicked.connect(self.getOutput)        
        
    def getInput(self):
       file = QFileDialog.getExistingDirectory(self, "Open Input Folder", "")
       if file:
           self.ui.input.setText(file)    
    def getOutput(self):
        file = QFileDialog.getExistingDirectory(self, "Open Output Folder", "")
        if file:
            self.ui.output.setText(file)
            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    args = app.arguments()[1:]
    window = MainWindow(args)
    sys.exit(app.exec_())