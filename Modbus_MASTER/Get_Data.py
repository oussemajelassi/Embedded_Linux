# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetData.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

Items_Array = ["temp","ouss"]




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 308)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 411, 171))
        self.listWidget.setObjectName("listWidget")


        self.BUT_GET = QtWidgets.QPushButton(self.centralwidget)
        self.BUT_GET.setGeometry(QtCore.QRect(115, 199, 191, 41))
        self.BUT_GET.setObjectName("BUT_GET")
        self.BUT_GET.clicked.connect(self.Get_Data_Callback)

        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.BUT_GET.setText(_translate("MainWindow", "Get Data"))
    
    def Insert_Items (self , Items_Array) :
        _translate = QtCore.QCoreApplication.translate
        for Slave in (Items_Array) :
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            item.setText(_translate("MainWindow", str(Slave.Name)))
            

            

    def Get_Data_Callback(self) :
        print("Selected items: ", self.listWidget.selectedItems()[0].text())
        
        

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Insert_Items(Items_Array)
    MainWindow.show()
    sys.exit(app.exec_())
