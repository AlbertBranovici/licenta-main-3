from generatePasswordUI import *
from generatePasswordUI import generatePasswordUI

class entryDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Edit Entry")
        layout = QFormLayout(self)
        # generate = generatePasswordUI
        self.passwordGenerator = generatePasswordUI()
        self.passwordGenerator.passwordGenerated.connect(self.completePassword)

        self.titleEdit = QLineEdit(self)
        self.userEdit = QLineEdit(self)
        self.passwordEdit = QLineEdit(self)
        self.passwordRepeatEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordRepeatEdit.setEchoMode(QLineEdit.Password)
        self.urlEdit = QLineEdit(self)
        self.notesEdit = QLineEdit(self)
        # password layout
        passwordLayout = QHBoxLayout()
        showPasswordButton = QPushButton("Show", self)
        showPasswordButton.clicked.connect(self.toggle_password_visibility)
        passwordLayout.addWidget(self.passwordEdit)
        passwordLayout.addWidget(showPasswordButton)

        # repeat password layout
        passwordRepeatLayout = QHBoxLayout()

        # ------------
        generatePasswordButton = QPushButton("Generate", self)
        generatePasswordButton.clicked.connect(self.openPasswordGenerator)
        # ----------------

        passwordRepeatLayout.addWidget(self.passwordRepeatEdit)
        passwordRepeatLayout.addWidget(generatePasswordButton)

        # layout.add
        layout.addRow(QLabel("Title:"), self.titleEdit)
        layout.addRow(QLabel("Username:"), self.userEdit)
        layout.addRow(QLabel("Password:"), passwordLayout)
        layout.addRow(QLabel("Repeat:"), passwordRepeatLayout)
        layout.addRow(QLabel("URL:"), self.urlEdit)
        layout.addRow(QLabel("Notes:"), self.notesEdit)

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.ok_clicked)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

    def completePassword(self, password):
        self.passwordEdit.setText(password)
        self.passwordRepeatEdit.setText(password)
    def openPasswordGenerator(self):
        try:
            self.passwordGenerator.exec_()
        except Exception as e:
            print(e)

    def toggle_password_visibility(self):
        if self.passwordEdit.echoMode() == QLineEdit.Password:
            self.passwordEdit.setEchoMode(QLineEdit.Normal)
            self.passwordRepeatEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QLineEdit.Password)
            self.passwordRepeatEdit.setEchoMode(QLineEdit.Password)
    def ok_clicked(self):
        if self.passwordEdit.text() == self.passwordRepeatEdit.text():
            self.accept()
        else:
            QMessageBox.warning(self, 'Warning', 'The passwords do not match')
    def setData(self,data):
        self.titleEdit.setText(data['Title'])
        self.userEdit.setText(data['Username'])
        self.passwordEdit.setText(data['Password'])
        self.passwordRepeatEdit.setText(data['Password'])
        self.urlEdit.setText(data['URL'])
        self.notesEdit.setText(data['Notes'])

    def data(self):
        # aici se returneaza valorile introduse in QLineEdit pentru adaugare/modificare in tabela
        return {
            'Title': self.titleEdit.text(),
            'User Name': self.userEdit.text(),
            'Password': self.passwordEdit.text(),
            'URL': self.urlEdit.text(),
            'Notes': self.notesEdit.text()
        }