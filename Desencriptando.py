
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

class Ui_DialogDesencriptando(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(319, 145)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(152, 185, 255);"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.progressBarDesencriptando = QtGui.QProgressBar(Dialog)
        self.progressBarDesencriptando.setGeometry(QtCore.QRect(110, 40, 191, 23))
        self.progressBarDesencriptando.setProperty("value", 24)
        self.progressBarDesencriptando.setObjectName(_fromUtf8("progressBarDesencriptando"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 100, 75, 23))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Desencriptando...", None))
        self.label.setText(_translate("Dialog", "Desencriptando...", None))
        self.pushButton.setText(_translate("Dialog", "Cancelar", None))

