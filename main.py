import os
import sys
from platform import system
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QStyleFactory, QDesktopWidget, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from ruba_project_1.src import inspect_model

# Application root location ↓
if system() == "Windows":
    appFolder = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\"


class App(QMainWindow):
    def __init__(self):
        """Constructor."""
        super(App, self).__init__()
        uic.loadUi(appFolder + "ui design/interface_v2.ui",
                   self)  # Load the UI(User Interface) file.
        self.main()
        self.makeWindowCenter()
        # Status Bar Message
        self.statusBar().showMessage("Detect Phising Sites")
        self.setWindowTitle("Phising Detection App")
        self.night_mode = False

    def makeWindowCenter(self):
        """For launching windows in center."""
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def main(self):
        print("Ruba")
        """Main load function"""
        self.checkButton.clicked.connect(self.checkButtonEvent)
        self.clearButton.clicked.connect(self.clearButtonEvent)
        self.modeButton.clicked.connect(self.modeButtonEvent)

    def checkButtonEvent(self):
        user_url = self.urlBox.text()
        status, feature_values = inspect_model.main(user_url)
        print(status)
        if status == 0:
            QMessageBox.information(self, "Website Status",
                                    "Legitimate Website", QMessageBox.Ok)
        elif status == 1:
            QMessageBox.warning(self, "Website Status", "Phising Website",
                                QMessageBox.Ok)
        self.show_information_in_table(feature_values)

    def show_information_in_table(self, X):
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        # print(X[0])
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Feature Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Value"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Feature Name"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Value"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("HTTPS STATUS"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(str(X[0][0])))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("AT THE RATE CHECK"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem(str(X[0][1])))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("IP ADDRESS PRESENT"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem(str(X[0][2])))
        self.tableWidget.setItem(4, 0, QTableWidgetItem("DOT COUNT"))
        self.tableWidget.setItem(4, 1, QTableWidgetItem(str(X[0][3])))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("SLASH COUNT"))
        self.tableWidget.setItem(1, 3, QTableWidgetItem(str(X[0][4])))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("DASH CHECK"))
        self.tableWidget.setItem(2, 3, QTableWidgetItem(str(X[0][5])))
        self.tableWidget.setItem(3, 2, QTableWidgetItem("LENGTH OF HOST NAME"))
        self.tableWidget.setItem(3, 3, QTableWidgetItem(str(X[0][6])))
        self.tableWidget.setItem(4, 2, QTableWidgetItem("SLASH CHECK"))
        self.tableWidget.setItem(4, 3, QTableWidgetItem(str(X[0][7])))

    def clearButtonEvent(self):
        self.urlBox.clear()
        self.tableWidget.clear()

    def modeButtonEvent(self):
        # print("Button Clicked")
        if self.night_mode == False:
            self.modeButton.setText("Light")
            self.loadDarkMode()
            self.night_mode = True

        elif self.night_mode:
            self.modeButton.setText("Dark")
            self.loadLightMode()
            self.night_mode = False

    def loadDarkMode(self):
        app.setStyle(QStyleFactory.create("Fusion"))
        darkPalette = QtGui.QPalette()
        darkColor = QColor(45, 45, 45)
        disabledColor = QColor(127, 127, 127)
        darkPalette.setColor(QPalette.Window, darkColor)
        darkPalette.setColor(QPalette.WindowText, Qt.white)
        darkPalette.setColor(QPalette.Base, QColor(40, 40, 40))
        darkPalette.setColor(QPalette.AlternateBase, darkColor)
        darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
        darkPalette.setColor(QPalette.ToolTipText, Qt.white)
        darkPalette.setColor(QPalette.Text, Qt.white)
        darkPalette.setColor(QPalette.Disabled, QPalette.Text, disabledColor)
        darkPalette.setColor(QPalette.Button, darkColor)
        darkPalette.setColor(QPalette.ButtonText, Qt.white)
        darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText,
                             disabledColor)
        darkPalette.setColor(QPalette.BrightText, Qt.red)
        darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.HighlightedText, Qt.black)
        darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText,
                             disabledColor)
        app.setPalette(darkPalette)
        app.setStyleSheet(
            "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }"
        )

    def loadLightMode(self):
        darkPalette = QtGui.QPalette()
        darkColor = Qt.white
        disabledColor = QColor(45, 45, 45)
        darkPalette.setColor(QPalette.Window, QColor(242, 242, 242))
        darkPalette.setColor(QPalette.WindowText, Qt.black)
        darkPalette.setColor(QPalette.Base, Qt.white)
        darkPalette.setColor(QPalette.AlternateBase, darkColor)
        darkPalette.setColor(QPalette.ToolTipBase, Qt.black)
        darkPalette.setColor(QPalette.ToolTipText, Qt.black)
        darkPalette.setColor(QPalette.Text, Qt.black)
        darkPalette.setColor(QPalette.Disabled, QPalette.Text, disabledColor)
        darkPalette.setColor(QPalette.Button, darkColor)
        darkPalette.setColor(QPalette.ButtonText, Qt.black)
        darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText,
                             disabledColor)
        darkPalette.setColor(QPalette.BrightText, Qt.red)
        darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.HighlightedText, Qt.black)
        darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText,
                             disabledColor)
        app.setPalette(darkPalette)
        app.setStyleSheet(
            "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }"
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    main = App()  # Instantiate The App() class
    main.show()
    sys.exit(app.exec_())
