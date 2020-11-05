def clearButtonEvent(self):
    self.urlBox.clear()
    self.tableWidget.clear()

def modeButtonEvent(self):
    if night_mode:
        modeButton.setText("Light")
        self.loadDarkMode()
        night_mode = False

    elif night_mode == False:
        modeButton.setText("Dark")
        self.loadLightMode()
        night_mode = True

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
    darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, disabledColor)
    darkPalette.setColor(QPalette.BrightText, Qt.red)
    darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
    darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    darkPalette.setColor(QPalette.HighlightedText, Qt.black)
    darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, disabledColor)
    app.setPalette(darkPalette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

def loadLightMode(self):
    app.setStyle(QStyleFactory.create("Fusion"))
