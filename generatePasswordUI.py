from PyQt5.QtWidgets import QDialog
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal
from entryDialogUI import *
import random

class generatePasswordUI(QDialog):
    passwordGenerated = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        groupBox = QGroupBox("Settings")
        mainLayout = QVBoxLayout()

        # horizontal box for password length
        hbox = QHBoxLayout()
        lenLabel = QLabel("Length of password:")
        self.lenSpinBox = QSpinBox()
        self.lenSpinBox.setValue(15)
        hbox.addWidget(lenLabel)
        hbox.addWidget(self.lenSpinBox)

        # Values for each box
        self.upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.lowerCase = 'abcdefghijklmnopqrstuvwxyz'
        self.digits = '0123456789'
        self.underline = '_'
        self.special = '!@#$%^&*+=,.<>/|`~:;\\\'\"'
        self.minus = '-'
        self. space = ' '
        self.brackets = '[]{}()'

        # Grid for password options
        gridLayout = QGridLayout()
        self.upperCaseBox = QCheckBox("Uppercase(A, B, C, ...)")
        self.lowerCaseBox = QCheckBox("Lowercase(a, b, c, ...)")
        self.digitsBox = QCheckBox("Digits(1, 2, 3, ...")
        self.minusBox = QCheckBox("Minus( - )")
        self.underlineBox = QCheckBox("Underline( _ )")
        self.spaceBox = QCheckBox("Space(  )")
        self.specialBox = QCheckBox("Special(!, $, %, ...)")
        self.bracketsBox= QCheckBox("Brackets( [, ], {, }, ...)")

        gridLayout.addWidget(self.upperCaseBox, 0, 0)
        gridLayout.addWidget(self.lowerCaseBox, 0, 1)
        gridLayout.addWidget(self.digitsBox, 1, 0)
        gridLayout.addWidget(self.minusBox, 1, 1)
        gridLayout.addWidget(self.underlineBox, 2, 0)
        gridLayout.addWidget(self.spaceBox, 2, 1)
        gridLayout.addWidget(self.specialBox, 3, 0)
        gridLayout.addWidget(self.bracketsBox, 3, 1)

        generateButton = QPushButton("Generate")
        generateButton.clicked.connect(self.btn_clicked)

        self.reviewPassword = QTextEdit()
        self.reviewPassword.setReadOnly(True)
        self.reviewPassword.setBaseSize(100,100)
        reviewPasswordLabel = QLabel("Review")

        mainLayout.addLayout(hbox)
        mainLayout.addLayout(gridLayout)
        mainLayout.addWidget(generateButton)
        mainLayout.addWidget(reviewPasswordLabel)
        mainLayout.addWidget(self.reviewPassword)
        groupBox.setLayout(mainLayout)

        self.setLayout(mainLayout)
    def btn_clicked(self):
        string = ''
        b = False
        length = self.lenSpinBox.value()
        try:
            if self.upperCaseBox.isChecked():
                string += self.upperCase
                b = True
            if self.lowerCaseBox.isChecked():
                string += self.lowerCase
                b = True
            if self.digitsBox.isChecked():
                string += self.digits
                b = True
            if self.minusBox.isChecked():
                string += self.minus
                b = True
            if self.underlineBox.isChecked():
                string += self.underline
                b = True
            if self.spaceBox.isChecked():
                string += self.space
                b = True
            if self.specialBox.isChecked():
                string += self.special
                b = True
            if self.bracketsBox.isChecked():
                string += self.brackets
                b = True
            if b:
                self.generatePassword(string, length)
            else:
                QMessageBox.warning(self, 'Warning', 'Please select at least character set! ')
        except Exception as e:
            print(f"An error occurred: {e}")
        # return password


    def generatePassword(self, charSet, length):
        samples =''
        try:
            if not charSet:
                QMessageBox.warning(self, 'Warning', 'Character set is empty. Select at least one type of character.')
                return
            password = ''.join(random.choices(charSet, k=length))
            for i in range(10):
                samples += ''.join(random.choices(charSet, k=length))+'\n\n'
            self.reviewPassword.setText(samples)
            self.passwordGenerated.emit(password)
        except Exception as e:
            print(f"An error occurred: {e}")
