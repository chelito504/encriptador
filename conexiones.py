# -*- coding: utf-8 -*-
import sys
import os.path as path
from mainEncript import *
from BusquedaOpen import *
from ContrasenaOpen import *

class Principal(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.uiPrincipal = Ui_Dialog()
		self.uiPrincipal.setupUi(self)
		QtCore.QObject.connect(self.uiPrincipal.toolButtonOrigen, QtCore.SIGNAL('clicked()'), self.abrirBusqueda)
		QtCore.QObject.connect(self.uiPrincipal.toolButtonDestino, QtCore.SIGNAL('clicked()'), self.abrirBusqueda)
		QtCore.QObject.connect(self.uiPrincipal.pushButtonEncriptarAES, QtCore.SIGNAL('clicked()'), self.abrirEncriptamientoAES)
		QtCore.QObject.connect(self.uiPrincipal.pushButton, QtCore.SIGNAL('clicked()'), self.salirPrincipal)
	def abrirEncriptamientoAES(self):
		self.objectContra = PedirCotrasenaParaEncriptar()
		if (path.exists(self.uiPrincipal.lineEditOrigen.text()) and path.exists(self.uiPrincipal.lineEditDestino.text())):
			self.objectContra.mostrarContrasenaParaEncriptar()
			self.uiPrincipal.lineEditOrigen.clear()
			self.uiPrincipal.lineEditDestino.clear()
			self.uiPrincipal.label_3.clear()
		else:
			self.uiPrincipal.label_3.setText('ERROR: comprobar ruta/s')
	def abrirBusqueda(self):
		self.objectBusqueda = Busqueda()
		self.objectBusqueda.mostrarBusqueda()
	def salirPrincipal(self):
		sys.exit()

class Busqueda:
	def mostrarBusqueda(self):
		self.objectBusquedaOpen = Busqueda2()
		self.objectBusquedaOpen.show()

class PedirCotrasenaParaEncriptar:
	def mostrarContrasenaParaEncriptar(self):
		self.objectPedirContrasenaParaEncriptar = ContrasenaEnc()
		self.objectPedirContrasenaParaEncriptar.show()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Principal()
	myapp.show()
	sys.exit(app.exec_())
