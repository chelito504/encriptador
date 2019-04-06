# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic

'''class Principal(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("EncrpDesencrp.ui", self)
	def showEvent(self, event):
		self.labelBienvenida.setText("Bienvendio al encriptador/desencriptador de archivos")
	def closeEvent(self, event):
		pregunta = QMessageBox.question(self, "SALIR", "¿Seguro que quiere salir?", QMessageBox.Yes | QMessageBox.No)
		if pregunta == QMessageBox.Yes: event.accept()
		else: event.ignore() '''
principal = uic.loadUiType("EncrpDesencrp.ui")[0]
buscando = uic.loadUiType("Busqueda.ui")[0]

class MyWindowClass(QtGui.QMainWindow, principal):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		#self.toolButtonOrigen.clicked.connect(self.MySearching)

	def MySearching(self):
		#msc = MySearchingClass()
		'''app1 = QtGui.QApplication(sys.argv)
		search = MySearching
		search.show()
		app1.exec_()'''
		appQMainWindow = QtGui.QApplication(sys.argv)
		MyWindow = MyWindowClass(None)
		MyWindow.show()
		appQMainWindow.exec_()

class MySearchingClass(QtGui.QDialog, buscando):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.setupUi(self)
		appQDialogSearching = QtGui.QApplication(sys.argv)
		MySearch = MyWindowClass(None)
		MySearch.show()
		appQDialogSearching.exec_()

appQMainWindow = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
appQMainWindow.exec_()
