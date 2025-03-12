from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from views.agregarUsuario import Ui_Dialog #usuario

from model.Objects.Usuario import Usuario
from model.DAO.UsuarioDao import UsuarioDAO
from dbConnection.VerifyConnection import VerifyConnection

class AgregarUsuarioController(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        print("Agregar usuario")
        self.ui = Ui_Dialog()
        self.usuario_dao = UsuarioDAO()
        self.ui.setupUi(self)
        self.initializeGUI()

    # Initialize elements, for example, setting up button functionality
    def initializeGUI(self):

        self.ui.btnAgregar.clicked.connect(self.agregarUsuario)
        #pending
    def agregarUsuario(self):
        try:
            #update view so it can work
            iD = self.ui.leiD.text() #iD
            nombre = self.ui.leNombre.text()
            email = self.ui.leEmail.text()

            new_usuario = Usuario(iD, nombre, email) #Create object libro

            if VerifyConnection.verify_connection(self):
                #create libro dao
                self.usuario_dao.add_usuario(new_usuario)

                if self.usuario_dao.usuario_ref is not None:
                    QMessageBox.information(self, 'Confirmtion', 'A new user has been registered ✔', QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Error", "Cannot connect to Firebase. Check yout internet connection.", QMessageBox.Ok)
            else:
                QMessageBox.critical(self,"Error","No internet connection. Please check your connection.", QMessageBox.Ok)
            
            self.clearFields()
        except Exception as e:
            print(f"Error : {e}")
            QMessageBox.critical(self, "Error", "An unexpected error occurred while adding user.", QMessageBox.Ok)
     
    #check function bellow        
    def clearFields(self):
        self.ui.leiD.clear()
        self.ui.leNombre.clear()
        self.ui.leEmail.clear()