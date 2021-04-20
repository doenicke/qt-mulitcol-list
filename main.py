import uuid
from PyQt5 import QtWidgets, uic
import logging.config
import sys

logging.basicConfig()
logger = logging.getLogger(__name__)


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = uic.loadUi('main_window.ui', self)

        self.ui.label.setText('')
        # self.ui.treeWidget.setColumnCount(2)
        self.ui.treeWidget.setHeaderLabels(['ID', 'Text'])

        # Connect clicks to functions:
        self.ui.btnAdd.clicked.connect(self.add_item)
        self.ui.btnEdit.clicked.connect(self.edit_item)
        self.ui.btnDelete.clicked.connect(self.delete_item)
        self.ui.treeWidget.itemSelectionChanged.connect(self.get_item_data)

    def delete_item(self):
        try:
            get_selected = self.ui.treeWidget.selectedItems()[0]
        except:
            return
        idx = self.ui.treeWidget.indexOfTopLevelItem(get_selected)
        print("deleting index:", idx)
        self.ui.treeWidget.takeTopLevelItem(idx)

    def edit_item(self):
        try:
            get_selected = self.ui.treeWidget.selectedItems()[0]
        except:
            return
        get_selected.setText(1, self.ui.lineEdit.text())

    def add_item(self):
        if not self.ui.lineEdit.text():
            return

        item = QtWidgets.QTreeWidgetItem()
        item.setText(0, str(uuid.uuid1()))
        item.setText(1, self.ui.lineEdit.text())
        try:
            self.ui.treeWidget.addTopLevelItem(item)
        except Exception as e:
            print(e)

    def get_item_data(self):
        try:
            item = list(self.ui.treeWidget.selectedItems())[0]
        except:
            return
        self.ui.label.setText(item.text(0))
        self.ui.lineEdit.setText(item.text(1))
        print("selected:", item.text(0), item.text(1))


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    sys.excepthook = except_hook
    main()
