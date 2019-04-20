# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainEncript.ui'
#
# Created: Wed Apr 17 21:37:42 2019
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(759, 547)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(152, 185, 255);"))
        self.toolButtonOrigen = QtGui.QToolButton(Dialog)
        self.toolButtonOrigen.setGeometry(QtCore.QRect(260, 40, 25, 19))
        self.toolButtonOrigen.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.toolButtonOrigen.setObjectName(_fromUtf8("toolButtonOrigen"))
        self.toolButtonDestino = QtGui.QToolButton(Dialog)
        self.toolButtonDestino.setGeometry(QtCore.QRect(260, 70, 25, 19))
        self.toolButtonDestino.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.toolButtonDestino.setObjectName(_fromUtf8("toolButtonDestino"))
        self.lineEditOrigen = QtGui.QLineEdit(Dialog)
        self.lineEditOrigen.setGeometry(QtCore.QRect(110, 40, 141, 20))
        self.lineEditOrigen.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEditOrigen.setObjectName(_fromUtf8("lineEditOrigen"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEditDestino = QtGui.QLineEdit(Dialog)
        self.lineEditDestino.setGeometry(QtCore.QRect(110, 70, 141, 20))
        self.lineEditDestino.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEditDestino.setObjectName(_fromUtf8("lineEditDestino"))
        self.pushButtonEncriptarAES = QtGui.QPushButton(Dialog)
        self.pushButtonEncriptarAES.setGeometry(QtCore.QRect(54, 130, 111, 23))
        self.pushButtonEncriptarAES.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonEncriptarAES.setObjectName(_fromUtf8("pushButtonEncriptarAES"))
        self.pushButtonEncriptarOtro = QtGui.QPushButton(Dialog)
        self.pushButtonEncriptarOtro.setGeometry(QtCore.QRect(50, 230, 111, 23))
        self.pushButtonEncriptarOtro.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonEncriptarOtro.setObjectName(_fromUtf8("pushButtonEncriptarOtro"))
        self.pushButtonDesencriptarAES = QtGui.QPushButton(Dialog)
        self.pushButtonDesencriptarAES.setGeometry(QtCore.QRect(54, 180, 111, 23))
        self.pushButtonDesencriptarAES.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonDesencriptarAES.setObjectName(_fromUtf8("pushButtonDesencriptarAES"))
        self.pushButtonDesencriptarOtro = QtGui.QPushButton(Dialog)
        self.pushButtonDesencriptarOtro.setGeometry(QtCore.QRect(50, 280, 111, 23))
        self.pushButtonDesencriptarOtro.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonDesencriptarOtro.setObjectName(_fromUtf8("pushButtonDesencriptarOtro"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 330, 75, 23))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 380, 261, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.treeWidgetOrigen = QtGui.QTreeWidget(Dialog)
        self.treeWidgetOrigen.setGeometry(QtCore.QRect(390, 40, 291, 231))
        self.treeWidgetOrigen.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.treeWidgetOrigen.setObjectName(_fromUtf8("treeWidgetOrigen"))
        self.treeWidgetDestino = QtGui.QTreeWidget(Dialog)
        self.treeWidgetDestino.setGeometry(QtCore.QRect(390, 290, 291, 231))
        self.treeWidgetDestino.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.treeWidgetDestino.setObjectName(_fromUtf8("treeWidgetDestino"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "ENDEAR v 2.0", None))
        self.toolButtonOrigen.setText(_translate("Dialog", "...", None))
        self.toolButtonDestino.setText(_translate("Dialog", "...", None))
        self.label_2.setText(_translate("Dialog", "Destino", None))
        self.label.setText(_translate("Dialog", "Origen", None))
        self.pushButtonEncriptarAES.setText(_translate("Dialog", "Encriptar AES-256", None))
        self.pushButtonEncriptarOtro.setText(_translate("Dialog", "Encriptar otro", None))
        self.pushButtonDesencriptarAES.setText(_translate("Dialog", "Desencriptar AES-256", None))
        self.pushButtonDesencriptarOtro.setText(_translate("Dialog", "Desencriptar otro", None))
        self.pushButton.setText(_translate("Dialog", "Salir", None))
        self.treeWidgetOrigen.headerItem().setText(0, _translate("Dialog", "Nombre", None))
        self.treeWidgetOrigen.headerItem().setText(1, _translate("Dialog", "Fecha modificación", None))
        self.treeWidgetOrigen.headerItem().setText(2, _translate("Dialog", "Tipo", None))
        self.treeWidgetOrigen.headerItem().setText(3, _translate("Dialog", "Tamaño", None))
        self.treeWidgetDestino.headerItem().setText(0, _translate("Dialog", "Nombre", None))
        self.treeWidgetDestino.headerItem().setText(1, _translate("Dialog", "Fecha modificación", None))
        self.treeWidgetDestino.headerItem().setText(2, _translate("Dialog", "Tipo", None))
        self.treeWidgetDestino.headerItem().setText(3, _translate("Dialog", "Tamaño", None))


