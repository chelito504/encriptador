# -*- coding: utf-8 -*-
import sys
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
	def comprobarOrigen(self):
		if self.uiPrincipal.lineEditOrigen.isEmpty():
			return False
		else:
			return True
	def comprobarDestino(self):
		if self.uiPrincipal.lineEditDestino.isEmpty():
			return False
		else:
			return True
	def abrirBusqueda(self):
		self.vBusqueda = Busqueda()
		self.vBusqueda.mostrar()
	def salirPrincipal(self):
		sys.exit()
	def abrirEncriptarAes(self):
		self.vEncriptamiento1 = Encriptamiento1()
		if self.comprobarOrigen==True and self.comprobarDestino==True:
			self.vEncriptamiento1.mostrar()
		else:
			self.uiPrincipal.label_3.setText('ERROR: origen, destino u origen y destino vacías')

class Busqueda:
	def mostrar(self):
		self.objectBusquedaOpen = Busqueda2()
		self.objectBusquedaOpen.show()
class Encriptamiento1:
	def mostrar(self):
		self.objectEncriptarAesOpen = EncriptarAES()
		self.objectEncriptarAesOpen.show()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Principal()
	myapp.show()
	sys.exit(app.exec_())
