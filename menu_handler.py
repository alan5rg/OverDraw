from PyQt5.QtWidgets import QMainWindow, QMenuBar

class MenuHandler(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent

    def createMenu(self):
        # Crear menú
        mainMenu = QMenuBar(self.main_window)   
        trazo_menu = mainMenu.addMenu('&Trazo')

        #self.main_window.mainMenu = QMenuBar(self.main_window)   
        #trazo_menu = self.main_window.mainMenu.addMenu('&Trazo')

        # Crear menú
        #trazo_menu = self.main_window.QMenuBar().addMenu('Trazo')

        # Opciones de color
        color_action = trazo_menu.addAction('Color')
        color_action.triggered.connect(self.main_window.button_handler.color_dialog)