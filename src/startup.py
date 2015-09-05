#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15/09/05

import sys
from PyQt5 import QtGui, QtWidgets
from main import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnAddWord.clicked.connect(self.btnAddWordClicked)
        self.btnClear.clicked.connect(self.btnClearClicked)

    def btnAddWordClicked(self):
        pass

    def btnClearClicked(self):
        self.textWord.setPlainText(u'')
        self.textPronun.setPlainText(u'')
        self.textGrammar.setPlainText(u'')
        self.textDef.setPlainText(u'')
        self.textExample.setPlainText(u'')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyApp()
    # w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Vocabulary Generator')
    w.show()
    sys.exit(app.exec_())
