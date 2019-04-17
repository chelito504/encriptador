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

class Ui_DialogKey(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(317, 142)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(152, 185, 255);"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 181, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEditPwKey = QtGui.QLineEdit(Dialog)
        self.lineEditPwKey.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.lineEditPwKey.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEditPwKey.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPwKey.setObjectName(_fromUtf8("lineEditPwKey"))
        self.pushButtonCancelarKey = QtGui.QPushButton(Dialog)
        self.pushButtonCancelarKey.setGeometry(QtCore.QRect(210, 100, 75, 23))
        self.pushButtonCancelarKey.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonCancelarKey.setObjectName(_fromUtf8("pushButtonCancelarKey"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Key", None))
        self.label.setText(_translate("Dialog", "Ingrese su contraseña:", None))
        self.pushButtonCancelarKey.setText(_translate("Dialog", "Cancelar", None))

