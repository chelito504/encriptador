# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Busqueda.ui'
#
# Created: Tue Apr 09 23:07:11 2019
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

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(354, 280)
        dialog.setStyleSheet(_fromUtf8("background-color: rgb(152, 185, 255);"))
        self.treeView = QtGui.QTreeView(dialog)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 281, 211))
        self.treeView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.pushButtonOkBusqueda = QtGui.QPushButton(dialog)
        self.pushButtonOkBusqueda.setGeometry(QtCore.QRect(10, 240, 71, 23))
        self.pushButtonOkBusqueda.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonOkBusqueda.setObjectName(_fromUtf8("pushButtonOkBusqueda"))
        self.pushButtonCancelarBusqueda = QtGui.QPushButton(dialog)
        self.pushButtonCancelarBusqueda.setGeometry(QtCore.QRect(90, 240, 71, 23))
        self.pushButtonCancelarBusqueda.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonCancelarBusqueda.setObjectName(_fromUtf8("pushButtonCancelarBusqueda"))

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "Búsqueda", None))
        self.pushButtonOkBusqueda.setText(_translate("dialog", "OK", None))
        self.pushButtonCancelarBusqueda.setText(_translate("dialog", "Cancelar", None))
