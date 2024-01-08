

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 711, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/krpre/OneDrive/Pictures/Nitro/Nitro_Wallpaper_01_3840x2400.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushAcer = QtWidgets.QPushButton(self.centralwidget)
        self.pushAcer.setGeometry(QtCore.QRect(20, 510, 121, 28))
        self.pushAcer.setObjectName("pushAcer")
        self.pushYoutube = QtWidgets.QPushButton(self.centralwidget)
        self.pushYoutube.setGeometry(QtCore.QRect(662, 507, 111, 31))
        self.pushYoutube.setObjectName("pushYoutube")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushAcer.clicked.connect(self.show_Acer)
        self.pushYoutube.clicked.connect(self.show_Youtube)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushAcer.setText(_translate("MainWindow", "Acer"))
        self.pushYoutube.setText(_translate("MainWindow", "Youtube"))

    def show_Acer(self):
        self.label.setPixmap(QtGui.QPixmap("C:/Users/krpre/OneDrive/Pictures/Nitro/Nitro_Wallpaper_01_3840x2400.jpg"))
    
    def show_Youtube(self):
        self.label.setPixmap(QtGui.QPixmap("D:/VSCODE/HTML-CSS/Youtube-clone/thumbnails/thumbnail-1.webp"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
