import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
# from windowMain import *
from windowMain import MainWin
from criptare import *


class saveDialogUI(QDialog):
    def __init__(self, parent = None, mainWin=None):
        super().__init__(parent)
        self.setWindowTitle("Save Data")
        self.mainWin = mainWin if mainWin is not None else MainWin()
        layout = QFormLayout(self)
        # self.tableData = self.mainWin.tableDataSignal.connect(self.handle_data)
        # self.file_path = self.mainWin.file_path

        passwordLayout = QHBoxLayout()
        passwordLabel = QLabel(self)
        passwordLabel.setText("Set a password:")
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        passwordLayout.addWidget(passwordLabel)
        passwordLayout.addWidget(self.passwordEdit)

        passwordRepeatLayout = QHBoxLayout()
        passwordRepeatLabel = QLabel(self)
        passwordRepeatLabel.setText("Repeat password:")
        self.passwordRepeatEdit = QLineEdit(self)
        self.passwordRepeatEdit.setEchoMode(QLineEdit.Password)

        passwordRepeatLayout.addWidget(passwordRepeatLabel)
        passwordRepeatLayout.addWidget(self.passwordRepeatEdit)

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.ok_clicked)

        layout.addRow(passwordLayout)
        layout.addRow(passwordRepeatLayout)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

    def ok_clicked(self):
        try:
            file_path = self.mainWin.file_path
            if self.passwordEdit.text() == self.passwordRepeatEdit.text():
                tableData = self.mainWin.get_table_data()
                primaryKey = self.passwordEdit.text()

                encrypt_and_save(tableData, primaryKey,file_path)
                self.accept()
            else:
                QMessageBox.warning(self, 'Warning', 'The passwords do not match')
        except Exception as e:
            print(e)

