# -*- coding: utf-8 -*-
import sys
import os.path as path
from mainEncript import *
from BusquedaOpen import *
from EncriptarAesOpen import *

class Principal(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.uiPrincipal = Ui_Dialog()
		self.uiPrincipal.setupUi(self)
		QtCore.QObject.connect(self.uiPrincipal.toolButtonOrigen, QtCore.SIGNAL('clicked()'), self.abrirBusqueda)
		QtCore.QObject.connect(self.uiPrincipal.toolButtonDestino, QtCore.SIGNAL('clicked()'), self.abrirBusqueda)
		QtCore.QObject.connect(self.uiPrincipal.pushButtonEncriptarAES, QtCore.SIGNAL('clicked()'), self.abrirEncriptarAes)
		QtCore.QObject.connect(self.uiPrincipal.pushButton, QtCore.SIGNAL('clicked()'), self.salirPrincipal)
	def comprobarExistenciaOrigen(self):
		if path.exists(self.uiPrincipal.lineEditOrigen.text()):
			return True
		else:
			return False
	def comprobarExistenciaDestino(self):
		if path.exists(self.uiPrincipal.lineEditDestino.text()):
			return True
		else:
			return False
	def abrirBusqueda(self):
		self.objectBusqueda = Busqueda()
		self.objectBusqueda.mostrarBusqueda()
	def salirPrincipal(self):
		sys.exit()
	def abrirEncriptarAes(self):
		self.objectEncriptamiento1 = EncriptamientoAES()
		if self.comprobarExistenciaOrigen==True and self.comprobarExistenciaDestino==True:
			self.objectEncriptamiento1.mostrarEncriptamientoAES()
		else:
			self.uiPrincipal.label_3.setText('ERROR: path inexistente')
class Busqueda:
	def mostrarBusqueda(self):
		self.objectBusquedaOpen = Busqueda2()
		self.objectBusquedaOpen.show()
class EncriptamientoAES:
	def mostrarEncriptamientoAES(self):
		self.objectEncriptarAesOpen = EncriptarAES()
		self.objectEncriptarAesOpen.show()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Principal()
	myapp.show()
	sys.exit(app.exec_())
