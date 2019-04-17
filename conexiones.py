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
		QtCore.QObject.connect(self.uiPrincipal.pushButtonEncriptarAES, QtCore.SIGNAL('clicked()'), self.abrirEncriptamiento)
		QtCore.QObject.connect(self.uiPrincipal.pushButton, QtCore.SIGNAL('clicked()'), self.salirPrincipal)
	def abrirEncriptamiento(self):
		#if len(self.uiPrincipal.lineEditOrigen.text())==0:
		#	return 0
		#else:
		self.objectEncriptamiento1 = EncriptamientoAES()
		if (path.exists(self.uiPrincipal.lineEditOrigen.text()) and path.exists(self.uiPrincipal.lineEditDestino.text())):
			self.objectEncriptamiento1.mostrarEncriptamientoAES()
			self.uiPrincipal.lineEditOrigen.clear()
			self.uiPrincipal.lineEditDestino.clear()
		else:
			self.uiPrincipal.label_3.setText('ERROR: comprobar ruta/s')
	#def comprobarExistenciaDestino(self):
		#if len(self.uiPrincipal.lineEditDestino.text())==0:
		#	return 0
		#else:
		#if path.exists(self.uiPrincipal.lineEditDestino.text()):
		#	return True
		#else:
		#	return False
	def abrirBusqueda(self):
		self.objectBusqueda = Busqueda()
		self.objectBusqueda.mostrarBusqueda()
	def salirPrincipal(self):
		sys.exit()
	#def abrirEncriptarAes(self):
	#	if(self.comprobarExistenciaOrigen==True and self.comprobarExistenciaDestino==True):
	#		self.objectEncriptamiento1 = EncriptamientoAES()
	#		self.objectEncriptamiento1.mostrarEncriptamientoAES()
	#		self.uiPrincipal.lineEditOrigen.clear()
	#		self.uiPrincipal.lineEditDestino.clear()
		#elif(self.comprobarExistenciaOrigen==True and self.comprobarExistenciaDestino==False):
		#	self.uiPrincipal.label_3.setText('ERROR: verificar destino')
		#elif(self.comprobarExistenciaOrigen==False and self.comprobarExistenciaDestino==True):
		#	self.uiPrincipal.label_3.setText('ERROR: verificar origen')
	#	else:
		#if (self.comprobarExistenciaOrigen==False and self.comprobarExistenciaDestino==False):
	#		self.uiPrincipal.label_3.setText('ERROR: verificar ambas rutas')
		#elif (self.comprobarExistenciaOrigen==0 and self.comprobarExistenciaDestino==0):
		#	self.uiPrincipal.label_3.setText('ERROR: ambas rutas vacias')
		#else:
			#self.objectEncriptamiento1.mostrarEncriptamientoAES()
			#self.uiPrincipal.lineEditOrigen.clear()
			#self.uiPrincipal.lineEditDestino.clear()
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
