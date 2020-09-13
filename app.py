import sys
from PyQt5 import QtWidgets
from gui import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(486,433)

        with open('data.txt') as f:
            for row in f:
                self.ui.listWidget.addItems([row.strip()])

        self.ui.pushButton.clicked.connect(self.add)
        self.ui.lineEdit.returnPressed.connect(self.add)
        self.ui.listWidget.itemDoubleClicked.connect(self.remove)

    def add(self):
        print("Neuer Eintrag")
        self.ui.listWidget.addItems([self.ui.lineEdit.text()])
        self.ui.lineEdit.setText("")

        self.update_file()

    def remove(self, item):
        self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
        self.update_file()

    def update_file(self):    
        with open('data.txt',"w") as f:
            for x in range(self.ui.listWidget.count()):
                f.write(self.ui.listWidget.item(x).text()+"\n")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = MyApp()
    form.show()
    sys.exit(app.exec_())