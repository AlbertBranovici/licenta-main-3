from windowMain import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWin()
    demo.show()
    sys.exit(app.exec_())