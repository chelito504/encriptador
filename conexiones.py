# -*- coding: utf-8 -*-
import sys, time
import os.path as path
from mainEncript import *
from ContrasenaOpen import *
from os import listdir, path, stat
from mimetypes import MimeTypes
from time import time
from Crypto.Cipher import AES

class Principal(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.uiPrincipal = Ui_Dialog()
		self.uiPrincipal.setupUi(self)
		QtCore.QObject.connect(self.uiPrincipal.toolButtonOrigen, QtCore.SIGNAL('clicked()'), self.verRutasOrigen)
		QtCore.QObject.connect(self.uiPrincipal.toolButtonDestino, QtCore.SIGNAL('clicked()'), self.verRutasDestino)
		QtCore.QObject.connect(self.uiPrincipal.pushButtonEncriptarAES, QtCore.SIGNAL('clicked()'), self.abrirEncriptamientoAES)
		QtCore.QObject.connect(self.uiPrincipal.pushButton, QtCore.SIGNAL('clicked()'), self.salirPrincipal)
		QtCore.QObject.connect(self.uiPrincipal.pushButtonDesencriptarAES, QtCore.SIGNAL('clicked()'), self.abrirDesencriptamientoAES)
		QtCore.QObject.connect(self.uiPrincipal.treeWidgetOrigen, QtCore.SIGNAL('itemDoubleClicked()'), self.abrirElementoOrigen)
		QtCore.QObject.connect(self.uiPrincipal.pushButtonEncriptarOtro, QtCore.SIGNAL('clicked()'), self.encriptarOtro)

'''	

	def prueba(self):
		self.inicio = time()
		for i in range(10001):
			self.editarLabel(str(i))
		self.fin = time()
		print self.getEficiencia(self.inicio, self.fin)

'''
	def encriptarOtro(self):
		pass

	def abrirEncriptamientoAES(self):
		self.objectContra = PedirCotrasenaParaEncriptar()
		if (path.exists(self.uiPrincipal.lineEditOrigen.text()) and path.exists(self.uiPrincipal.lineEditDestino.text())):
			self.objectContra.mostrarContrasenaParaEncriptar()
			self.limpiarLabel()
		elif(path.exists(self.uiPrincipal.lineEditOrigen.text()) and len(self.uiPrincipal.lineEditDestino.text())==0):
			self.editarDestino(self.uiPrincipal.lineEditOrigen.text())
		else:
			self.editarLabel('ERROR: comprobar ruta/s')
	def abrirDesencriptamientoAES(self):
		self.objectContraDes = PedirCotrasenaParaDesencriptar()
		if(path.exists(self.uiPrincipal.lineEditOrigen.text()) and path.exists(self.uiPrincipal.lineEditDestino.text())):
			self.objectContraDes.mostrarContrasenaParaDesencriptar()
			self.limpiarLabel()
	def verRutasOrigen(self):
		self.uiPrincipal.treeWidgetOrigen.clear()
		dir = self.uiPrincipal.lineEditOrigen.text()
		if path.isdir(dir):
			for element in listdir(dir):
				name = element
				pathinfo = dir+'\\'+name
				informacion = stat(pathinfo)
				if path.isdir(pathinfo):
					type = 'Carpeta de archivos'
					size = ''
				else:
					mime = MimeTypes()
					type = mime.guess_type(pathinfo)[0]
					size = str(informacion.st_size)+' bytes'
				date = str(time.ctime(informacion.st_mtime))
				row = [name, date, type, size]
				self.uiPrincipal.treeWidgetOrigen.insertTopLevelItems(0, [QtGui.QTreeWidgetItem(self.uiPrincipal.treeWidgetOrigen, row)])
	def verRutasDestino(self):
		self.uiPrincipal.treeWidgetDestino.clear()
		dir1 = self.uiPrincipal.lineEditDestino.text()
		if path.isdir(dir1):
			for element1 in listdir(dir1):
				name1 = element1
				pathinfo1 = dir1+'\\'+name1
				informacion1 = stat(pathinfo1)
				if path.isdir(pathinfo1):
					type1 = 'Carpeta de archivos'
					size1 = ''
				else:
					mime1 = MimeTypes()
					type1 = mime1.guess_type(pathinfo1)[0]
					size1 = str(informacion1.st_size)+' bytes'
				date1 = str(time.ctime(informacion1.st_mtime))
				row1 = [name1, date1, type1, size1]
				self.uiPrincipal.treeWidgetDestino.insertTopLevelItems(0, [QtGui.QTreeWidgetItem(self.uiPrincipal.treeWidgetDestino, row1)])
	def abrirElementoOrigen(self):
		item = self.uiPrincipal.treeWidgetOrigen.currentItem()
		elemento = self.uiPrincipal.lineEditOrigen.text()+'\\'+item.text(0)
		if path.isdir(elemento):
			self.editarOrigen(elemento)
			self.getDir()
		else:
			self.editarLabel('ERROR')
	def getEficiencia(self, inicio, fin):
		return self.fin-self.inicio
	def salirPrincipal(self):
		sys.exit()

#Algunos métodos:
	def limpiarLinesEdit(self):
		self.uiPrincipal.lineEditOrigen.clear()
		self.uiPrincipal.lineEditDestino.clear()
	def limpiarLabel(self):
		self.uiPrincipal.label_3.clear()
	def editarLabel(self, texto):
		self.uiPrincipal.label_3.setText(texto)
	def editarOrigen(self, texto):
		self.uiPrincipal.lineEditOrigen.setText(texto)
	def editarDestino(self, texto):
		self.uiPrincipal.lineEditDestino.setText(texto)

class PedirCotrasenaParaEncriptar:
	def mostrarContrasenaParaEncriptar(self):
		self.objectPedirContrasenaParaEncriptar = ContrasenaEnc()
		self.objectPedirContrasenaParaEncriptar.show()

class PedirContrasenaParaDesencriptar:
	def mostrarContrasenaParaDesencriptar(self):
		self.objectPedirContrasenaParaDesencriptar = ContrasenaDes()
		self.objectPedirContrasenaParaDesencriptar.show()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Principal()
	myapp.show()
	sys.exit(app.exec_())
