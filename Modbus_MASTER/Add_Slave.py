# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddSlave.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

Modbus_Slaves = []
class Modbus_Slave () : 
    def __init__(self,Name,Ip,Port) -> None:
        self.Name = Name
        self.Ip = Ip
        self.Port = Port

class Ui_Add_Slave(object):

    global Modbus_Slaves
    def setupUi(self, Add_Slave):
        Add_Slave.setObjectName("Add_Slave")
        Add_Slave.resize(320, 279)
        self.centralwidget = QtWidgets.QWidget(Add_Slave)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.IpAdress = QtWidgets.QTextEdit(self.centralwidget)
        self.IpAdress.setGeometry(QtCore.QRect(160, 10, 141, 41))
        self.IpAdress.setObjectName("IpAdress")
        
        
        self.Port = QtWidgets.QTextEdit(self.centralwidget)
        self.Port.setGeometry(QtCore.QRect(160, 70, 141, 41))
        self.Port.setObjectName("Port")
        
        
        self.Name = QtWidgets.QTextEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(160, 130, 141, 41))
        self.Name.setObjectName("Name")
        
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 121, 31))
        self.label_3.setObjectName("label_3")
        
        self.BUT_Save = QtWidgets.QPushButton(self.centralwidget)
        self.BUT_Save.setGeometry(QtCore.QRect(80, 180, 131, 41))
        self.BUT_Save.setObjectName("BUT_Save")
        self.BUT_Save.clicked.connect(self.Slave_Added_Callback)
        
        
        Add_Slave.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Add_Slave)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 26))
        self.menubar.setObjectName("menubar")
        Add_Slave.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Add_Slave)
        self.statusbar.setObjectName("statusbar")
        Add_Slave.setStatusBar(self.statusbar)

        self.retranslateUi(Add_Slave)
        QtCore.QMetaObject.connectSlotsByName(Add_Slave)

    def retranslateUi(self, Add_Slave):
        _translate = QtCore.QCoreApplication.translate
        Add_Slave.setWindowTitle(_translate("Add_Slave", "AddSlave"))
        self.IpAdress.setHtml(_translate("Add_Slave", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Add_Slave", "IP Address "))
        self.label_2.setText(_translate("Add_Slave", "Port Number"))
        self.label_3.setText(_translate("Add_Slave", "Name"))
        self.BUT_Save.setText(_translate("Add_Slave", "Add"))

    def Slave_Added_Callback (self) :
        New_Slave = Modbus_Slave(self.Name.toPlainText(),self.IpAdress.toPlainText(),self.Port.toPlainText())
        Modbus_Slaves.append(New_Slave)
        self.Name.clear()
        self.IpAdress.clear()
        self.Port.clear()
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_Slave = QtWidgets.QMainWindow()
    ui = Ui_Add_Slave()
    ui.setupUi(Add_Slave)
    Add_Slave.show()
    sys.exit(app.exec_())
