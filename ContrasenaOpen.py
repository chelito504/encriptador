# -*- coding: utf-8 -*-

import sys 
from Contrasena import *
from EncriptarAesOpen import * 

class ContrasenaEnc(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.uiContrasenaEnc = Ui_DialogContrasena()
		self.uiContrasenaEnc.setupUi(self)
		QtCore.QObject.connect(self.uiContrasenaEnc.pushButtonOkContrasena, QtCore.SIGNAL('clicked()'), self.encriptarAES)
	def encriptarAES(self):
		self.objectEncriptar1 = EncriptamientoAES()
		if(self.uiContrasenaEnc.lineEditPwContrasena.text()==self.uiContrasenaEnc.lineEditDeNuevoContrasena.text()):
			self.objectEncriptar1.mostrarEncriptamientoAES()
			self.uiContrasenaEnc.label_3.clear()
		else:
			self.uiContrasenaEnc.label_3.setText('Contrasenas distintas')
			self.uiContrasenaEnc.lineEditPwContrasena.clear()
			self.uiContrasenaEnc.lineEditDeNuevoContrasena.clear()

class EncriptamientoAES:
	def mostrarEncriptamientoAES(self):
		self.objectEncriptarAesOpen = EncriptarAES()
		self.objectEncriptarAesOpen.show()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = ContrasenaEnc()
	myapp.show()
	sys.exit(app.exec_())
