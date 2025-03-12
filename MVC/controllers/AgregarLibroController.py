from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from views.agregarLibro import Ui_Dialog

from model.Objects.Libro import Libro
from model.DAO.LibroDao import LibroDAO
from dbConnection.VerifyConnection import VerifyConnection

class AgregarLibroController(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        print("Agregar Libro")
        self.ui = Ui_Dialog()
        self.libro_dao = LibroDAO()
        self.ui.setupUi(self)
        self.initializeGUI()

    # Initialize elements, for example, setting up button functionality
    def initializeGUI(self):

        self.ui.btnAgregar.clicked.connect(self.agregarLibro)
        #pending
    def agregarLibro(self):
        try:
            #update view so it can work
            titulo = self.ui.leTitulo.text()
            autor = self.ui.leAutor.text()
            genero = self.ui.leGenero.text()
            disponible = self.ui.leDisponible.text()

            new_libro = Libro(titulo, autor, genero, disponible) #Create object libro

            if VerifyConnection.verify_connection(self):
                #create libro dao
                self.libro_dao.add_libro(new_libro)

                if self.libro_dao.libro_ref is not None:
                    QMessageBox.information(self, 'Confirmtion', 'A new book has been registered ✔', QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Error", "Cannot connect to Firebase. Check yout internet connection.", QMessageBox.Ok)
            else:
                QMessageBox.critical(self,"Error","No internet connection. Please check your connection.", QMessageBox.Ok)
            
            self.clearFields()
        except Exception as e:
            print(f"Error : {e}")
            QMessageBox.critical(self, "Error", "An unexpected error occurred while adding book.", QMessageBox.Ok)
     
    #check function bellow        
    def clearFields(self):
        self.ui.leTitulo.clear()
        self.ui.leAutor.clear()
        self.ui.leGenero.clear()
        self.ui.leDisponible.clear()
