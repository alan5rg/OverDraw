from PyQt5.QtWidgets import QPushButton, QWidget, QColorDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import sip #,QPainter, QPen,

class ButtonHandler(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent
        self.overlay_status = False
        self.lastcolor = '#000000'
        self.status_pen = True

    def createButtons(self):
        self.ancho = self.main_window.frameSize().width()
        self.createControlButtons()
        self.createPenButtons()
        self.createOverlayButtons()

    def createControlButtons(self):
        # Botones relacionados con el control de la ventana
        self.mostrar_button = QPushButton('Mostrar Ctrl', self.main_window)
        self.mostrar_button.clicked.connect(lambda: self.mostrar_ctrl(True))
        self.mostrar_button.setMaximumHeight(20)
        self.mostrar_button.move(self.ancho - 110, 10)
        self.mostrar_button.setVisible(False)
        
        self.ocultar_button = QPushButton('Ocultar Ctrl', self.main_window)
        self.ocultar_button.clicked.connect(lambda: self.mostrar_ctrl(False))
        self.ocultar_button.setMaximumHeight(20)
        self.ocultar_button.move(self.ancho - 110, 10)
                
        self.minimize_button = QPushButton('Minimizar', self.main_window)
        self.minimize_button.clicked.connect(self.main_window.showMinimized)
        self.minimize_button.setMaximumHeight(20)
        self.minimize_button.move(10, 10)

        self.restore_button = QPushButton('Restaurar', self.main_window)
        self.restore_button.clicked.connect(self.main_window.showNormal)
        self.restore_button.setMaximumHeight(20)
        self.restore_button.move(110, 10)

        self.maximize_button = QPushButton('Maximizar', self.main_window)
        self.maximize_button.clicked.connect(self.main_window.showMaximized)
        self.maximize_button.setMaximumHeight(20)
        self.maximize_button.move(210, 10)

        self.close_button = QPushButton('Cerrar', self.main_window)
        self.close_button.clicked.connect(self.main_window.close)
        self.close_button.setMaximumHeight(20)
        self.close_button.move(310, 10)

    def createPenButtons(self):
        # Botones relacionados con el lápiz
        self.mostrar_pen_button = QPushButton('Mostrar Pen', self.main_window)
        self.mostrar_pen_button.clicked.connect(lambda: self.mostrar_pen(True))
        self.mostrar_pen_button.setFixedHeight(50)
        self.mostrar_pen_button.move(self.ancho - 110, 50)
        self.mostrar_pen_button.setVisible(False)
        
        self.ocultar_pen_button = QPushButton('Ocultar Pen', self.main_window)
        self.ocultar_pen_button.clicked.connect(lambda: self.mostrar_pen(False))
        self.ocultar_pen_button.setFixedHeight(50)
        self.ocultar_pen_button.move(self.ancho - 110, 50)

        self.borrar_button = QPushButton('Borrar', self.main_window)
        self.borrar_button.clicked.connect(self.borrar_dibujo)
        self.borrar_button.setMaximumHeight(20)
        self.borrar_button.move(10, 50)

        self.mas_button = QPushButton('+Grosor', self.main_window)
        self.mas_button.clicked.connect(self.mas_grosor)
        self.mas_button.setMaximumHeight(20)
        self.mas_button.move(110, 50)

        self.menos_button = QPushButton('-Grosor', self.main_window)
        self.menos_button.clicked.connect(self.menos_grosor)
        self.menos_button.setMaximumHeight(20)
        self.menos_button.move(210, 50)

        self.rojo_button = QPushButton('Trazo Rojo', self.main_window)
        self.rojo_button.clicked.connect(lambda: self.trazo_color(255,0,0))
        self.rojo_button.setMaximumHeight(20)
        self.rojo_button.move(10, 80)

        self.verde_button = QPushButton('Trazo Verde', self.main_window)
        self.verde_button.clicked.connect(lambda: self.trazo_color(0,255,0))
        self.verde_button.setMaximumHeight(20)
        self.verde_button.move(110, 80)

        self.azul_button = QPushButton('Trazo Azul', self.main_window)
        self.azul_button.clicked.connect(lambda: self.trazo_color(0,0,255))
        self.azul_button.setMaximumHeight(20)
        self.azul_button.move(210, 80)

        self.tgrosor_dialog_button = QPushButton('Selec Grosor', self.main_window)
        self.tgrosor_dialog_button.clicked.connect(lambda: self.grosor_dialog())
        self.tgrosor_dialog_button.setMaximumHeight(20)
        self.tgrosor_dialog_button.move(410, 50)

        self.tcolor_dialog_button = QPushButton('Selec Color', self.main_window)
        self.tcolor_dialog_button.clicked.connect(lambda: self.color_dialog())
        self.tcolor_dialog_button.setMaximumHeight(20)
        self.tcolor_dialog_button.move(410, 80)

        self.lapis_select_button = QPushButton('Lápiz', self.main_window)
        self.lapis_select_button.clicked.connect(lambda: self.shape_select("Lápiz"))
        self.lapis_select_button.setMaximumHeight(20)
        self.lapis_select_button.move(510, 50)

        self.linea_select_button = QPushButton('Línea', self.main_window)
        self.linea_select_button.clicked.connect(lambda: self.shape_select("Línea"))
        self.linea_select_button.setMaximumHeight(20)
        self.linea_select_button.move(510, 80)

    def createOverlayButtons(self):
        # Botones relacionados con el fondo
        self.mostrar_over_button = QPushButton('Mostrar Over', self.main_window)
        self.mostrar_over_button.clicked.connect(lambda: self.mostrar_over(True))
        self.mostrar_over_button.setFixedHeight(50)
        self.mostrar_over_button.move(self.ancho - 110, 120)
        self.mostrar_over_button.setVisible(False)
        
        self.ocultar_over_button = QPushButton('Ocultar Over', self.main_window)
        self.ocultar_over_button.clicked.connect(lambda: self.mostrar_over(False))
        self.ocultar_over_button.setFixedHeight(50)
        self.ocultar_over_button.move(self.ancho - 110, 120)

        self.overlay_button = QPushButton('Overlay On/Off', self.main_window)
        self.overlay_button.clicked.connect(self.overlay_control)
        self.overlay_button.setMaximumHeight(20)
        self.overlay_button.move(10, 135)

        self.fondo_rojo_button = QPushButton('Fondo Rojo', self.main_window)
        self.fondo_rojo_button.clicked.connect(lambda: self.fondo_color('#FF0000'))
        self.fondo_rojo_button.setMaximumHeight(20)
        self.fondo_rojo_button.move(110, 120)

        self.fondo_verde_button = QPushButton('Fondo Verde', self.main_window)
        self.fondo_verde_button.clicked.connect(lambda: self.fondo_color('#00FF00'))
        self.fondo_verde_button.setMaximumHeight(20)
        self.fondo_verde_button.move(210, 120)

        self.fondo_azul_button = QPushButton('Fondo Azul', self.main_window)
        self.fondo_azul_button.clicked.connect(lambda: self.fondo_color('#0000FF'))
        self.fondo_azul_button.setMaximumHeight(20)
        self.fondo_azul_button.move(310, 120)

        self.fondo_blanco_button = QPushButton('Fondo Blanco', self.main_window)
        self.fondo_blanco_button.clicked.connect(lambda: self.fondo_color('#FFFFFF'))
        self.fondo_blanco_button.setMaximumHeight(20)
        self.fondo_blanco_button.move(110, 150)
        
        self.fondo_negro_button = QPushButton('Fondo Negro', self.main_window)
        self.fondo_negro_button.clicked.connect(lambda: self.fondo_color('#000000'))
        self.fondo_negro_button.setMaximumHeight(20)
        self.fondo_negro_button.move(210, 150)

        self.fondo_gris_button = QPushButton('Fondo Gris', self.main_window)
        self.fondo_gris_button.clicked.connect(lambda: self.fondo_color('#808080'))
        self.fondo_gris_button.setMaximumHeight(20)
        self.fondo_gris_button.move(310, 150)

        self.redibujar_circulo()
        self.mostrar_ctrl(False)
        self.mostrar_pen(False)
        self.mostrar_over(False)

    def mostrar_ctrl(self,mostrar:bool):
        self.ocultar_button.setVisible(mostrar)
        self.minimize_button.setVisible(mostrar)
        self.maximize_button.setVisible(mostrar)
        self.restore_button.setVisible(mostrar)
        self.close_button.setVisible(mostrar)
        if not mostrar:
            self.mostrar_button.setVisible(True)
    def mostrar_pen(self, mostrar:bool):
        self.status_pen = mostrar
        self.ocultar_pen_button.setVisible(mostrar)
        self.borrar_button.setVisible(mostrar)
        self.mas_button.setVisible(mostrar)
        self.menos_button.setVisible(mostrar)
        self.rojo_button.setVisible(mostrar)
        self.verde_button.setVisible(mostrar)
        self.azul_button.setVisible(mostrar)
        self.tcolor_dialog_button.setVisible(mostrar)
        self.lapis_select_button.setVisible(mostrar)
        self.linea_select_button.setVisible(mostrar)
        self.tgrosor_dialog_button.setVisible(mostrar)
        if not mostrar:
            self.mostrar_pen_button.setVisible(True)
            self.borrar_circulo()
        else:
            self.redibujar_circulo()

    def mostrar_over(self,mostrar:bool):
        self.ocultar_over_button.setVisible(mostrar)
        self.overlay_button.setVisible(mostrar)
        self.fondo_rojo_button.setVisible(mostrar)
        self.fondo_verde_button.setVisible(mostrar)
        self.fondo_azul_button.setVisible(mostrar)
        self.fondo_blanco_button.setVisible(mostrar)
        self.fondo_negro_button.setVisible(mostrar)
        self.fondo_gris_button.setVisible(mostrar)
        if not mostrar:
            self.mostrar_over_button.setVisible(True)

    def borrar_dibujo(self):
        self.main_window.drawing_view.scene().clear()
        self.main_window.drawing_view.current_circle = None
        self.redibujar_circulo()
    
    def trazo_color(self, r:int, g:int, b:int):
        self.main_window.drawing_view.pen.setColor(QColor(r,g,b))
        self.redibujar_circulo()

    def color_dialog(self):
        color = QColorDialog.getColor(self.main_window.drawing_view.pen.color(), self, 'Color del Trazo')
        if color.isValid():
            self.main_window.drawing_view.pen.setColor(color)
            self.redibujar_circulo()

    def shape_select(self, shape:str):
        self.main_window.drawing_view.select_shape = shape

    def mas_grosor(self):
        self.main_window.drawing_view.pen.setWidthF(self.main_window.drawing_view.pen.widthF()+1)
        self.redibujar_circulo()
    def menos_grosor(self):
        if self.main_window.drawing_view.pen.widthF() > 2.0:
            self.main_window.drawing_view.pen.setWidthF(self.main_window.drawing_view.pen.widthF()-1)
        self.redibujar_circulo()

    def grosor_dialog(self):
        self.main_window.toolbar_handler.show_width_dialog()

    def redibujar_circulo(self):
        self.borrar_circulo()
        if self.status_pen: self.main_window.drawing_view.current_circle = self.main_window.drawing_view.scene().addEllipse(325, 40, 50, 50, self.main_window.drawing_view.pen)
    
    def borrar_circulo(self):
        if self.main_window.drawing_view.current_circle is not None:
            self.main_window.drawing_view.scene().removeItem(self.main_window.drawing_view.current_circle)
            self.main_window.drawing_view.current_circle = None

    def fondo_color(self,color:str):
        self.main_window.setAutoFillBackground(True)
        self.main_window.drawing_view.setStyleSheet(f"background-color: {color};") 
        self.lastcolor = color
        self.overlay_status = False
        self.overlay_control()

    def overlay_control(self):
        if self.overlay_status:
            self.main_window.drawing_view.setStyleSheet("background: transparent;")
            self.main_window.setAutoFillBackground(False)
            self.main_window.setAttribute(Qt.WA_TranslucentBackground)
            self.main_window.toolbar_handler.custom_toolbar_style()
            self.overlay_status = False
        else:
            self.main_window.drawing_view.setStyleSheet("background: solid;")
            self.main_window.drawing_view.setStyleSheet(f"background-color: {self.lastcolor};") 
            self.main_window.setStyleSheet("background: solid;")
            self.overlay_status = True
    