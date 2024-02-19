from PyQt5.QtGui import QIcon, QPainter, QColor
from PyQt5.QtWidgets import QMenu, QMenuBar
from entryDialogUI import *
from pathlib import Path
from criptare import *
import platform
# from saveDialogUI import saveDialogUI

class StarDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        text = index.data(Qt.DisplayRole)
        star_text = '*' * len(str(text))
        painter.drawText(option.rect, Qt.AlignCenter, star_text)
# class MainWin(QWidget):
class MainWin(QMainWindow):
    tableDataSignal = pyqtSignal(list)
    def __init__(self):
        super().__init__()


        self.setWindowTitle('Licenta')
        self.resize(686, 340)
        # --Table--
        self.table = QTableWidget(0,5,self)
        self.table.setHorizontalHeaderLabels(['Title', 'User Name', 'Password', 'URL', 'Notes'])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.contextMenu)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)
        delegate = StarDelegate(self)
        self.table.setItemDelegateForColumn(2, delegate)
        # --------

        self.file_path = ''
        # if platform.uname().system.startswith('Darw'):
        #     #     aici este pentru macOS
        #     menu = QMenuBar()
        # else:
        #     menu = QMenuBar(self)
        #     #     aici este pentru windows
        # # Menubar---
        tray = QSystemTrayIcon()
        menu = QMenuBar(self)
        menu.setNativeMenuBar(False)


        actionFile = menu.addMenu("&File")
        newFile = QAction("New", self)
        newFile.setShortcut("Ctrl+N")

        openFile = QAction("Open", self)
        openFile.setShortcut("Ctrl+O")
        openFile.triggered.connect(self.open_file)

        saveFile = QAction("Save", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.triggered.connect(self.save_data)
        close = QAction("Close", self)
        close.setShortcut("Ctrl+Q")

        actionFile.addAction(newFile)
        actionFile.addAction(openFile)
        actionFile.addAction(saveFile)
        actionFile.addAction(close)


        actionEntry = menu.addMenu("&Entry")
        # Se initializeaza actiunile care sunt adaugate in meniul Entry
        addEntryAction = QAction("Add Entry", self)
        copyUsername = QAction("Copy Username", self)
        copyPassword = QAction("Copy Password", self)
        # Se conecteaza fiecare optiune la o metoda
        addEntryAction.triggered.connect(self.addEntry)
        copyUsername.triggered.connect(self.copy_username)
        copyPassword.triggered.connect(self.copy_password)

        # Se adauga fiecare optiune in meniul actionEntry
        actionEntry.addAction(addEntryAction)
        actionEntry.addAction(copyUsername)
        actionEntry.addAction(copyPassword)

        #Icon menu bar
        iconMenu = QMenuBar(self)
        iconMenu.setNativeMenuBar(False)
        newAction = QAction(QIcon('icons/file-regular.svg'),'New File', self)

        saveAction = QAction(QIcon('icons/floppy-disk.svg'), 'Save File', self)
        saveAction.triggered.connect(self.save_data)

        openAction = QAction(QIcon('icons/folder-open.svg'), 'Open File', self)
        openAction.triggered.connect(self.open_file)

        copyUserAction = QAction(QIcon('icons/user.svg'), 'Copy Username', self)
        copyUserAction.triggered.connect(self.copy_username)

        copyPasswordAction = QAction(QIcon('icons/key.svg'), 'Copy Password', self)
        copyPasswordAction.triggered.connect(self.copy_password)

        menuSeparator = QAction('|',self)
        menuSeparator.setEnabled(False)

        iconMenu.addAction(newAction)
        iconMenu.addAction(saveAction)
        iconMenu.addAction(openAction)
        iconMenu.addAction(menuSeparator)
        # iconMenu.addSeparator()
        iconMenu.addAction(copyUserAction)
        iconMenu.addAction(copyPasswordAction)
        # iconMenu.addAction(menuSeparator)


        # tray.setContextMenu(menu)
        # tray.setContextMenu(iconMenu)
        self.setMenuBar(menu)
        layout = QGridLayout()
        layout.addWidget(menu, 0, 0)
        layout.addWidget(iconMenu,1,0)
        layout.addWidget(self.table,2,0)
        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)
        # layout.addWidget(menu,0,0)
        # layout.addWidget(iconMenu,1,0)
        # layout.addWidget(self.table,2,0)
        # self.setLayout(layout)

    def send_to_clipboard(self,text):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
    def copy_password(self):
        try:
            current_row = self.table.currentRow()
            password = self.table.item(current_row, 2).text()
            self.send_to_clipboard(password)
        except Exception as e:
            print(f"An error ocurred: {e}")
    def copy_username(self):
        try:
            current_row = self.table.currentRow()
            user = self.table.item(current_row,1).text()
            self.send_to_clipboard(user)
        except Exception as e:
            print(f"An error ocurred: {e}")

    def contextMenu(self, position):
        menu = QMenu()
        # Add actions to the menu
        editAction = menu.addAction("Edit Entry")
        removeAction = menu.addAction("Remove")
        addAction = menu.addAction("Add Entry")

        action = menu.exec_(self.table.viewport().mapToGlobal(position))

        if action == editAction:
            self.editEntry()
        elif action == removeAction:
            # Remove the selected row
            current_row = self.table.currentRow()
            self.table.removeRow(current_row)
        elif action == addAction:
            self.addEntry()
    def addEntry(self):
        try:
            row_number = self.table.rowCount()
            dialog = entryDialog(self)
            if dialog.exec_() == QDialog.Accepted:
                new_data = dialog.data()
                self.table.insertRow(row_number)
                for i, (key,value) in enumerate(new_data.items()):
                    self.table.setItem(row_number, i, QTableWidgetItem(value))
        except Exception as e:
            print(f"An error ocurred: {e}")
    def editEntry(self):
        try:
            current_row = self.table.currentRow()
            if current_row >= 0:
                current_data = {
                    'Title': self.table.item(current_row, 0).text() if self.table.item(current_row, 0) else "",
                    'Username': self.table.item(current_row, 1).text() if self.table.item(current_row, 1) else "",
                    'Password': self.table.item(current_row, 2).text() if self.table.item(current_row, 2) else "",
                    'URL': self.table.item(current_row, 3).text() if self.table.item(current_row, 3) else "",
                    'Notes': self.table.item(current_row, 4).text() if self.table.item(current_row, 4) else ""
                }
                dialog = entryDialog(self)
                dialog.setData(current_data)
                if dialog.exec_() == QDialog.Accepted:
                    new_data = dialog.data()
                    for i, (key, value) in enumerate(new_data.items()):
                        self.table.setItem(current_row, i, QTableWidgetItem(value))
        except Exception as e:
            print(f"An error ocurred: {e}")

    def get_table_data(self):
        rows = self.table.rowCount()
        cols = self.table.columnCount()
        data = []
        for row in range(rows):
            current_row_data = []
            for col in range(cols):
                item = self.table.item(row, col)
                if item is not None:
                    current_row_data.append(item.text())
                else:
                    current_row_data.append("")
            data.append(current_row_data)
        return data
    def open_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "All Files (*);;JSON Files (*.json)", options=options
        )
        if fileName:
            try:
                self.file_path = Path(fileName)
                from openDialogUI import openDialogUI
                openDialog = openDialogUI(self, mainWin=self)
                if openDialog.exec_() == QDialog.Accepted:
                    pass
            except Exception as e:
                print(e)


    def update_data(self, data):
        self.table.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for column_index, item_data in enumerate(row_data):
                item = QTableWidgetItem(str(item_data))
                self.table.setItem(row_index, column_index, item)

    def get_saveFile_path(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "All Files (*);;JSON Files (*.json)", options=options
        )
        if fileName:
            return fileName
        else:
            return

    def save_data(self):
        try:
            self.file_path = self.get_saveFile_path()
            if self.file_path is None:
                return
            from saveDialogUI import saveDialogUI
            save_dialog = saveDialogUI(self, mainWin=self)
            if save_dialog.exec_() == QDialog.Accepted:
                pass
        except Exception as e:
            print(e)
            return
