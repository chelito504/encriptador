
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
        Dialog.resize(318, 142)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(152, 185, 255);"))
        self.pushButtonOkContrasena = QtGui.QPushButton(Dialog)
        self.pushButtonOkContrasena.setGeometry(QtCore.QRect(30, 100, 75, 23))
        self.pushButtonOkContrasena.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonOkContrasena.setObjectName(_fromUtf8("pushButtonOkContrasena"))
        self.pushButtonCancelarContrasena = QtGui.QPushButton(Dialog)
        self.pushButtonCancelarContrasena.setGeometry(QtCore.QRect(120, 100, 75, 23))
        self.pushButtonCancelarContrasena.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonCancelarContrasena.setObjectName(_fromUtf8("pushButtonCancelarContrasena"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEditPwContrasena = QtGui.QLineEdit(Dialog)
        self.lineEditPwContrasena.setGeometry(QtCore.QRect(160, 20, 113, 20))
        self.lineEditPwContrasena.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEditPwContrasena.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPwContrasena.setObjectName(_fromUtf8("lineEditPwContrasena"))
        self.lineEditDeNuevoContrasena = QtGui.QLineEdit(Dialog)
        self.lineEditDeNuevoContrasena.setGeometry(QtCore.QRect(160, 50, 113, 20))
        self.lineEditDeNuevoContrasena.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEditDeNuevoContrasena.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditDeNuevoContrasena.setObjectName(_fromUtf8("lineEditDeNuevoContrasena"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Contraseña", None))
        self.pushButtonOkContrasena.setText(_translate("Dialog", "Ok", None))
        self.pushButtonCancelarContrasena.setText(_translate("Dialog", "Cancelar", None))
        self.label.setText(_translate("Dialog", "Ingrese una contraseña", None))
        self.label_2.setText(_translate("Dialog", "Ingrésela de nuevo", None))

