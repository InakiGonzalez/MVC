from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
#from controllers.AddNakamaController import AddNakamaController
from controllers.AgregarLibroController import AgregarLibroController
from controllers.AgregarUsuarioController import AgregarUsuarioController
from views.Home_View import Ui_Dialog

class HomeController(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("I'm adding a new book :D")
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.initializeGUI()

    # Initialize elements, for example, setting up button functionality
    def initializeGUI(self):

        self.ui.btnOpenAddLibro.clicked.connect(self.abrirAddLibro)
        self.ui.btnOpenAddUsuario.clicked.connect(self.abrirAddUsuario)

    def abrirAddLibro(self):

        firstController = AgregarLibroController()
        firstController.exec_()

    def abrirAddUsuario(self):
        secondController = AgregarUsuarioController()
        secondController.exec_()

    

