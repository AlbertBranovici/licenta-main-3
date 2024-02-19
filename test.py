from PyQt5.QtWidgets import QMainWindow, QAction, QToolTip, QApplication
from PyQt5.QtGui import QIcon
import sys

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        autoTypeAction = QAction(QIcon.fromTheme('document-save'), 'Auto-type', self)
        autoTypeAction.triggered.connect(self.autoTypeClicked)

        # Set tooltip using custom method
        self.setCustomToolTip(autoTypeAction, 'Perform Auto-Type Action')

        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(autoTypeAction)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Tooltip Example')
        self.show()

    def setCustomToolTip(self, widget, tooltip):
        widget.setToolTip(tooltip)
        QToolTip.showText(widget.mapToGlobal(widget.rect().center()), tooltip, widget)

    def autoTypeClicked(self):
        print('Auto-Type Action Clicked')

def main():
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
