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
        Dialog.resize(200, 76)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(152, 185, 255);"))
        self.pushButtonOkListo = QtGui.QPushButton(Dialog)
        self.pushButtonOkListo.setGeometry(QtCore.QRect(60, 40, 75, 23))
        self.pushButtonOkListo.setStyleSheet(_fromUtf8("background-color: rgb(255, 253, 229);"))
        self.pushButtonOkListo.setObjectName(_fromUtf8("pushButtonOkListo"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 161, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "¡Listo!", None))
        self.pushButtonOkListo.setText(_translate("Dialog", "Ok", None))
        self.label.setText(_translate("Dialog", "Acción completada con éxito", None))

