import os
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget #QPushButton, 
#from PyQt5.QtGui import QColor #,QPainter, QPen,
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from drawing_overlay import DrawingOverlay
from button_handler import ButtonHandler
from menu_handler import MenuHandler
from toolbar_handler import ToolbarHandler, WidthDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 800, 400)
        self.titulo = 'Alan5_OverDraw  v.0.8.5'
        self.setWindowTitle(self.titulo)
        self.setAttribute(Qt.WA_TranslucentBackground)

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.IconPath = os.path.join(scriptDir, 'icons')   
        self.setWindowIcon(QtGui.QIcon(self.IconPath + os.path.sep + 'overdraw.png'))
        
        self.drawing_view = DrawingOverlay(self)
        self.setCentralWidget(self.drawing_view)
        self.layout = QVBoxLayout(self.drawing_view)
        self.layout.addWidget(self.drawing_view)

        self.principal_UI()

    def principal_UI(self):
        

        self.button_handler = ButtonHandler(self)
        self.menu_handler = MenuHandler(self)
        self.toolbar_handler = ToolbarHandler(self)
        
        botones_feos = self.button_handler.createButtons()
        #barra_de_menu = self.menu_handler.createMenu()
        barra_de_herramientas = self.toolbar_handler.createToolbar()

        self.layout.addWidget(botones_feos)
        #self.layout.addWidget(barra_de_menu)
        self.layout.addWidget(barra_de_herramientas)

        '''
        self.widgets = self.findChildren(QWidget)
        for widget in self.widgets:
            print("wid:",widget,"nombre:",widget.objectName(),"en pos:", widget.pos(), "tamaño", widget.size())
        '''
        
        self.drawing_view.setAttribute(Qt.WA_AlwaysStackOnTop)
        
    
    def resizeEvent(self, event):
        ancho = event.size().width()
        self.button_handler.mostrar_button.move(ancho - 110, 10)
        self.button_handler.ocultar_button.move(ancho - 110, 10)
        self.button_handler.mostrar_over_button.move(ancho - 110, 120)
        self.button_handler.ocultar_over_button.move(ancho - 110, 120)
        self.button_handler.mostrar_pen_button.move(ancho - 110, 50)
        self.button_handler.ocultar_pen_button.move(ancho - 110, 50)
