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
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(152, 185, 255);"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 141, 20))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEditDestino = QtGui.QLineEdit(Dialog)
        self.lineEditDestino.setGeometry(QtCore.QRect(100, 80, 141, 20))
        self.lineEditDestino.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEditDestino.setObjectName(_fromUtf8("lineEditDestino"))
        self.radioButtonEncriptarAes256 = QtGui.QRadioButton(Dialog)
        self.radioButtonEncriptarAes256.setGeometry(QtCore.QRect(80, 120, 111, 17))
        self.radioButtonEncriptarAes256.setObjectName(_fromUtf8("radioButtonEncriptarAes256"))
        self.radioButtonEncriptarOtroMetodo = QtGui.QRadioButton(Dialog)
        self.radioButtonEncriptarOtroMetodo.setGeometry(QtCore.QRect(220, 120, 171, 17))
        self.radioButtonEncriptarOtroMetodo.setObjectName(_fromUtf8("radioButtonEncriptarOtroMetodo"))
        self.radioButtonDesencriptarAes256 = QtGui.QRadioButton(Dialog)
        self.radioButtonDesencriptarAes256.setGeometry(QtCore.QRect(80, 160, 131, 17))
        self.radioButtonDesencriptarAes256.setObjectName(_fromUtf8("radioButtonDesencriptarAes256"))
        self.radioButtonDesencriptarOtroMetodo = QtGui.QRadioButton(Dialog)
        self.radioButtonDesencriptarOtroMetodo.setGeometry(QtCore.QRect(220, 160, 161, 17))
        self.radioButtonDesencriptarOtroMetodo.setObjectName(_fromUtf8("radioButtonDesencriptarOtroMetodo"))
        self.pushButtonOk = QtGui.QPushButton(Dialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(100, 200, 75, 23))
        self.pushButtonOk.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.pushButtonSalir = QtGui.QPushButton(Dialog)
        self.pushButtonSalir.setGeometry(QtCore.QRect(220, 200, 75, 23))
        self.pushButtonSalir.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonSalir.setObjectName(_fromUtf8("pushButtonSalir"))
        self.toolButtonOrigen = QtGui.QToolButton(Dialog)
        self.toolButtonOrigen.setGeometry(QtCore.QRect(250, 50, 25, 19))
        self.toolButtonOrigen.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.toolButtonOrigen.setObjectName(_fromUtf8("toolButtonOrigen"))
        self.toolButtonDestino = QtGui.QToolButton(Dialog)
        self.toolButtonDestino.setGeometry(QtCore.QRect(250, 80, 25, 19))
        self.toolButtonDestino.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.toolButtonDestino.setObjectName(_fromUtf8("toolButtonDestino"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "ENDEAR v 1.4", None))
        self.label.setText(_translate("Dialog", "Origen", None))
        self.label_2.setText(_translate("Dialog", "Destino", None))
        self.radioButtonEncriptarAes256.setText(_translate("Dialog", "Encriptar AES-256", None))
        self.radioButtonEncriptarOtroMetodo.setText(_translate("Dialog", "Encriptar otro método", None))
        self.radioButtonDesencriptarAes256.setText(_translate("Dialog", "Desencriptar AES-256", None))
        self.radioButtonDesencriptarOtroMetodo.setText(_translate("Dialog", "Desencriptar otro método", None))
        self.pushButtonOk.setText(_translate("Dialog", "Ok", None))
        self.pushButtonSalir.setText(_translate("Dialog", "Salir", None))
        self.toolButtonOrigen.setText(_translate("Dialog", "...", None))
        self.toolButtonDestino.setText(_translate("Dialog", "...", None))

