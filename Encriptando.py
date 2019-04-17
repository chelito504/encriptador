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

class Ui_DialogEncriptando(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(317, 142)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(152, 185, 255);"))
        self.progressBarEncriptando = QtGui.QProgressBar(Dialog)
        self.progressBarEncriptando.setGeometry(QtCore.QRect(90, 50, 191, 23))
        self.progressBarEncriptando.setProperty("value", 24)
        self.progressBarEncriptando.setObjectName(_fromUtf8("progressBarEncriptando"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButtonCancelarEncriptando = QtGui.QPushButton(Dialog)
        self.pushButtonCancelarEncriptando.setGeometry(QtCore.QRect(210, 100, 75, 23))
        self.pushButtonCancelarEncriptando.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonCancelarEncriptando.setObjectName(_fromUtf8("pushButtonCancelarEncriptando"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Encriptando...", None))
        self.label.setText(_translate("Dialog", "Encriptando...", None))
        self.pushButtonCancelarEncriptando.setText(_translate("Dialog", "Cancelar", None))

