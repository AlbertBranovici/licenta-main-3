import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
# from windowMain import *
from windowMain import MainWin
from criptare import *


class openDialogUI(QDialog):
    def __init__(self, parent = None, mainWin=None):
        super().__init__(parent)
        self.setWindowTitle("Open Data Base")
        self.resize(240, 150)
        self.mainWin = mainWin if mainWin is not None else MainWin()
        layout = QFormLayout(self)

        passwordLayout = QHBoxLayout()
        passwordLabel = QLabel(self)
        passwordLabel.setText("Password:")
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        passwordLayout.addWidget(passwordLabel)
        passwordLayout.addWidget(self.passwordEdit)



        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.ok_clicked)



        layout.addRow(passwordLayout)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

    def ok_clicked(self):
        try:
            file_path = self.mainWin.file_path
            if self.passwordEdit.text() != "":
                masterKey = self.passwordEdit.text()
                if masterKey:
                    # aici se va face o verificare daca master Key este corect sau nu -- de studiat
                    data = read_and_decrypt(file_path, masterKey)
                    if data is None:
                        QMessageBox.warning(self, "Warning", "Incorrect password")
                    else:
                        self.mainWin.update_data(data)
                        self.accept()
            else:
                QMessageBox.warning(self, 'Warning', 'Please enter a password')
        except Exception as e:
            print(e)