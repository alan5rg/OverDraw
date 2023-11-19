import sys, os
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QSlider, QVBoxLayout, QDialogButtonBox, QDialog, QLabel, QComboBox
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import QSize

class WidthDialog(QDialog):
    def __init__(self, current_width, parent=None):
        super(WidthDialog, self).__init__(parent)
        self.main_window = parent
        self.current_width = current_width
        self.grosorUI()

    def grosorUI(self):
        self.setWindowTitle('Grosor de Línea')
        self.setFixedSize(300,120)
        #self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout()

        self.width_slider = QSlider(Qt.Horizontal)
        self.width_slider.setMinimum(1)
        self.width_slider.setMaximum(30)
        self.width_slider.setValue(self.current_width)
        self.width_slider.valueChanged.connect(self.update_label)

        self.width_label = QLabel('Grosor actual: {}'.format(self.current_width))

        #button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box = self.main_window.button_handler.CustomDialogButton(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        button_box.setMinimumSize(100,20)
        
        self.indic_label = QLabel('Selecciona el grosor de la línea:')
        layout.addWidget(self.indic_label)
        layout.addWidget(self.width_slider)
        layout.addWidget(self.width_label)
        layout.addWidget(button_box)
        self.setLayout(layout)

    def update_label(self):
        self.width_label.setText('Grosor actual: {}'.format(self.width_slider.value()))

    def selected_width(self):
        return self.width_slider.value()

class ShapeDialog(QDialog):
    def __init__(self, current_shape, parent=None):
        super(ShapeDialog, self).__init__(parent)
        self.main_window = parent
        self.current_shape = current_shape
        self.shapeUI()

    def shapeUI(self):
        self.setWindowTitle('Shape del Trazo')
        self.setFixedSize(300,120)

        layout = QVBoxLayout()

        self.shape_combo = QComboBox()
        shapes = self.main_window.drawing_view.shapes
        for shape in shapes:
            self.shape_combo.addItem(shape)
        self.shape_combo.setCurrentText(shapes[self.current_shape])

        #button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box = self.main_window.button_handler.CustomDialogButton(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        button_box.setMinimumSize(100,20)
        
        layout.addWidget(QLabel('Selecciona un shape para el trazo:'))
        layout.addWidget(self.shape_combo)
        layout.addWidget(button_box)
        self.setLayout(layout)

    def selected_shape(self):
        shapes = self.main_window.drawing_view.shapes
        return shapes.index(self.shape_combo.currentText())

class ToolbarHandler(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.IconPath = os.path.join(scriptDir, 'icons')

    def createToolbar(self):
        self.custom_toolbar_style()

        #toolbar personalizada
        self.tb = QToolBar("toolbar")
        self.tb = self.main_window.addToolBar("La Mejor &Toolbar del fukin mundo") #, Qt.TopToolBarArea)
        self.main_window.addToolBar(Qt.BottomToolBarArea, self.tb)
        #self.tb.setOrientation(QtCore.Qt.Vertical)
        #self.tb.setFixedWidth(500)
        #self.tb.setFixedHeight(50)
        #tb.setFloatable(True)
        #tb.setMovable(True)
        #self.addToolBarBreak()#Qt.TopToolBarArea) # or self.addToolBarBreak()
        self.tb.setIconSize(QSize(50, 50))

        #Selección de Color
        color = QAction(QIcon(self.IconPath + os.path.sep + 'paleta.png'), "Ventana de selección de &Color",self)
        color.setStatusTip('Ventana de selección de color')
        color.triggered.connect(self.main_window.button_handler.color_dialog)
        self.tb.addAction(color)

        #Selección de Grosor
        grosor = QAction(QIcon(self.IconPath + os.path.sep + 'grosorb.png'),"Ventana de selección de &Grosor de Trazo",self)
        grosor.setStatusTip('Ventana de selección de Grosor de Trazo')
        grosor.triggered.connect(self.show_width_dialog)
        self.tb.addAction(grosor)

        #Selección de shape
        shape = QAction(QIcon(self.IconPath + os.path.sep + 'shape.png'),"Ventana de selección de &Shape del Trazo",self)
        shape.setStatusTip('Ventana de selección de Shape del Trazo')
        shape.triggered.connect(self.show_shape_dialog)
        self.tb.addAction(shape)
        
        # Agrega un separador
        separador = QAction(QIcon(""), "", self)
        separador.setSeparator(True)
        self.tb.addAction(separador)

        #Borrar Dibujo
        borrar = QAction(QIcon(self.IconPath + os.path.sep + 'borrar.png'),"&Borrar Trazos",self)
        borrar.setStatusTip('Borrar Trazos')
        borrar.triggered.connect(self.borrar_trazos)
        self.tb.addAction(borrar)

        #Overlay Mode
        overlay = QAction(QIcon(self.IconPath + os.path.sep + 'overlay.png'),"Control Modo &Overlay",self)
        overlay.setStatusTip('Control Modo Overlay')
        overlay.triggered.connect(self.modo_overlay)
        self.tb.addAction(overlay)

        #Botones de Control
        botones = QAction(QIcon(self.IconPath + os.path.sep + 'ctrls.png'),"Mostrar/Ocultar Botones de Control",self)
        botones.setStatusTip('Mostrar/Ocultar Botones de Control')
        botones.triggered.connect(self.botones_control)
        self.tb.addAction(botones)

        # Agrega un separador
        separador = QAction(QIcon(""), "", self)
        separador.setSeparator(True)
        self.tb.addAction(separador)

        #Cerrar OverDraw
        cerrar = QAction(QIcon(self.IconPath + os.path.sep + 'cerrar.png'),"&Cerrar OverDraw",self)
        cerrar.setStatusTip('Cerrar OverDraw')
        cerrar.triggered.connect(self.main_window.close)
        self.tb.addAction(cerrar)
    
    def custom_toolbar_style(self):
        # Hoja de estilo para la QtoolBar
        toolbar_style = """
        QToolBar {
        background-color: black; /* Cambia a 'black' para hacerla negra */
        }
        QToolBar QToolButton {
        background-color: transparent;
        }
        QToolBar QToolButton:hover {
        background-color: rgba(30, 30, 30, 100); /* Cambia a 'black' para hacerlo negro */
        }
        QToolBar QToolButton:pressed {
        background-color: rgba(60, 60, 60, 100); /* Cambia a 'black' para hacerlo negro */
        }
        /*esta sección aplica estilo a las ventanas de dialogo*/
        QDialog {
        background-color: black;
        }
        QDialog QLabel{
        color: white;
        }
        QDialog QComboBox{
        background-color: black;
        color: white;
        }
        QDialog QComboBox::item {
        background-color: black;
        color: white;
        }
        QDialog QComboBox::item:selected {
        background-color: white;
        color: black;
        }
        """
        self.main_window.setStyleSheet(toolbar_style)

    def modo_overlay(self):
        self.main_window.button_handler.overlay_control()

    def botones_control(self):
        self.main_window.button_handler.mostrar_botones_control()

    def borrar_trazos(self):
        self.main_window.button_handler.borrar_dibujo()

    def apply_main_window_style(self, dialog):
        # Aplica el estilo de la ventana principal al diálogo
        dialog.setStyleSheet(self.main_window.styleSheet())

    def show_width_dialog(self):
        self.width_dialog = WidthDialog(self.main_window.drawing_view.pen.width(), self.main_window)
        self.apply_main_window_style(self.width_dialog)
        #self.width_dialog.setWindowModality(Qt.WindowModal)
        self.width_dialog.setWindowModality(Qt.ApplicationModal)
        self.width_dialog.show()
        self.width_dialog.accepted.connect(lambda: self.update_main_window("grosor"))

    def show_shape_dialog(self):
        shapes = self.main_window.drawing_view.shapes
        self.shape_dialog = ShapeDialog(shapes.index(self.main_window.drawing_view.select_shape), self.main_window)
        self.apply_main_window_style(self.shape_dialog)
        #self.shape_dialog.setWindowModality(Qt.WindowModal)
        self.shape_dialog.setWindowModality(Qt.ApplicationModal)
        self.shape_dialog.show()
        self.shape_dialog.accepted.connect(lambda: self.update_main_window("shape"))

    def update_main_window(self, que_cosa:str):
        if que_cosa == "grosor":
            selected_width = self.width_dialog.selected_width()
            if selected_width != self.main_window.drawing_view.pen.width():
                self.main_window.drawing_view.pen.setWidth(selected_width)
                self.main_window.button_handler.redibujar_circulo()
        if que_cosa == "shape":
            selected_shape = self.shape_dialog.selected_shape()
            if selected_shape != self.main_window.drawing_view.select_shape:
                shapes = self.main_window.drawing_view.shapes
                self.main_window.drawing_view.select_shape = shapes[selected_shape]
