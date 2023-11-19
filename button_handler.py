import sys, os
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QColorDialog, QApplication, QGraphicsDropShadowEffect, QDialogButtonBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap
import sip #,QPainter, QPen,

class ButtonHandler(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent
        self.overlay_status = False
        self.lastcolor = '#000000'
        self.btnctrl_status = True
        self.status_btns_ctrl = True
        self.status_btns_pen = True
        self.status_btns_over = True
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.IconPath = os.path.join(scriptDir, 'icons')   

    def createButtons(self):
        self.ancho = self.main_window.frameSize().width()
        self.createLogoApp()
        self.createControlButtons()
        self.createPenButtons()
        self.createOverlayButtons()
                
    def CustomButton(self, text, parent):
        boton = QPushButton(text, parent)
        self.sombrear_y_tunear(boton)
        return boton
    
    def CustomDialogButton(self, buttons):
        dialog_button_box = QDialogButtonBox(buttons)
        buttons = dialog_button_box.buttons()
        for button in buttons:
            self.sombrear_y_tunear(button)
        return dialog_button_box

    def sombrear_y_tunear(self, boton):
        # Crear un efecto de sombra
        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(5)
        sombra.setColor(QColor(128, 128, 128))
        sombra.setOffset(2, 2)
        # Aplicar el efecto de sombra al botón
        boton.setGraphicsEffect(sombra)
        # Aplicar otros estilos si es necesario
        boton.setStyleSheet("""
            QPushButton {
                /*text-transform: uppercase;*/
                font-style: normal;
                font-weight: bold;
                font-size: 13px;
                min-width: 95px;
                min-height: 20px;
                background: solid;
                background-color: white;
                /*background-color: lightgray;*/
                border: 1px solid darkgray;
                border-radius: 10px;
            }
        """)

    def createLogoApp(self):
        # Logo de la app
        logoPixmap = QPixmap(self.IconPath + os.path.sep + 'lovepen.png')
        self.logo_label = QLabel('Logo_label!!!', self.main_window)
        self.logo_label.setScaledContents(True)
        self.logo_label.setFixedSize(48,48)
        self.logo_label.setPixmap(logoPixmap)
        self.logo_label.move(337,50)
        # Establece estilo del logo con fondo transparente en cualquier tema de la app
        logo_style = (
            "background-color: rgba(0, 0, 0, 0);"
        )
        self.logo_label.setStyleSheet(logo_style)
        
    def createControlButtons(self):
        # Botones relacionados con el control de la ventana
        self.mostrar_ctrl_button = self.CustomButton('Mostrar Ctrl', self.main_window)
        self.mostrar_ctrl_button.clicked.connect(lambda: self.mostrar_ctrl(True))
        self.mostrar_ctrl_button.setMaximumHeight(20)
        self.mostrar_ctrl_button.move(self.ancho - 110, 10)
        
        self.ocultar_ctrl_button = self.CustomButton('Ocultar Ctrl', self.main_window)
        self.ocultar_ctrl_button.clicked.connect(lambda: self.mostrar_ctrl(False))
        self.ocultar_ctrl_button.setMaximumHeight(20)
        self.ocultar_ctrl_button.move(self.ancho - 110, 10)
                
        self.minimize_button = self.CustomButton('Minimizar', self.main_window)
        self.minimize_button.clicked.connect(self.main_window.showMinimized)
        self.minimize_button.setMaximumHeight(20)
        self.minimize_button.move(10, 10)

        self.restore_button = self.CustomButton('Restaurar', self.main_window)
        self.restore_button.clicked.connect(self.main_window.showNormal)
        self.restore_button.setMaximumHeight(20)
        self.restore_button.move(110, 10)

        self.maximize_button = self.CustomButton('Maximizar', self.main_window)
        self.maximize_button.clicked.connect(self.main_window.showMaximized)
        self.maximize_button.setMaximumHeight(20)
        self.maximize_button.move(210, 10)

        self.close_button = self.CustomButton('Cerrar', self.main_window)
        self.close_button.clicked.connect(self.main_window.close)
        self.close_button.setMaximumHeight(20)
        self.close_button.move(310, 10)

    def createPenButtons(self):
        # Botones relacionados con el lápiz
        self.mostrar_pen_button = self.CustomButton('Mostrar Pen', self.main_window)
        self.mostrar_pen_button.clicked.connect(lambda: self.mostrar_pen(True))
        self.mostrar_pen_button.setFixedHeight(50)
        self.mostrar_pen_button.move(self.ancho - 110, 50)
        
        self.ocultar_pen_button = self.CustomButton('Ocultar Pen', self.main_window)
        self.ocultar_pen_button.clicked.connect(lambda: self.mostrar_pen(False))
        self.ocultar_pen_button.setFixedHeight(50)
        self.ocultar_pen_button.move(self.ancho - 110, 50)

        self.borrar_button = self.CustomButton('Borrar', self.main_window)
        self.borrar_button.clicked.connect(self.borrar_dibujo)
        self.borrar_button.setMaximumHeight(20)
        self.borrar_button.move(10, 50)

        self.mas_button = self.CustomButton('+Grosor', self.main_window)
        self.mas_button.clicked.connect(self.mas_grosor)
        self.mas_button.setMaximumHeight(20)
        self.mas_button.move(110, 50)

        self.menos_button = self.CustomButton('-Grosor', self.main_window)
        self.menos_button.clicked.connect(self.menos_grosor)
        self.menos_button.setMaximumHeight(20)
        self.menos_button.move(210, 50)

        self.rojo_button = self.CustomButton('Trazo Rojo', self.main_window)
        self.rojo_button.clicked.connect(lambda: self.trazo_color(255,0,0))
        self.rojo_button.setMaximumHeight(20)
        self.rojo_button.move(10, 80)

        self.verde_button = self.CustomButton('Trazo Verde', self.main_window)
        self.verde_button.clicked.connect(lambda: self.trazo_color(0,255,0))
        self.verde_button.setMaximumHeight(20)
        self.verde_button.move(110, 80)

        self.azul_button = self.CustomButton('Trazo Azul', self.main_window)
        self.azul_button.clicked.connect(lambda: self.trazo_color(0,0,255))
        self.azul_button.setMaximumHeight(20)
        self.azul_button.move(210, 80)

        self.tgrosor_dialog_button = self.CustomButton('Selec Grosor', self.main_window)
        self.tgrosor_dialog_button.clicked.connect(lambda: self.grosor_dialog())
        self.tgrosor_dialog_button.setMaximumHeight(20)
        self.tgrosor_dialog_button.move(410, 50)

        self.tcolor_dialog_button = self.CustomButton('Selec Color', self.main_window)
        self.tcolor_dialog_button.clicked.connect(lambda: self.color_dialog())
        self.tcolor_dialog_button.setMaximumHeight(20)
        self.tcolor_dialog_button.move(410, 80)

        self.lapis_select_button = self.CustomButton('Lápiz', self.main_window)
        self.lapis_select_button.clicked.connect(lambda: self.shape_select("Lápiz"))
        self.lapis_select_button.setMaximumHeight(20)
        self.lapis_select_button.move(510, 50)

        self.linea_select_button = self.CustomButton('Línea', self.main_window)
        self.linea_select_button.clicked.connect(lambda: self.shape_select("Línea"))
        self.linea_select_button.setMaximumHeight(20)
        self.linea_select_button.move(510, 80)

    def createOverlayButtons(self):
        # Botones relacionados con el fondo
        self.mostrar_over_button = self.CustomButton('Mostrar Over', self.main_window)
        self.mostrar_over_button.clicked.connect(lambda: self.mostrar_over(True))
        self.mostrar_over_button.setFixedHeight(50)
        self.mostrar_over_button.move(self.ancho - 110, 120)
        
        self.ocultar_over_button = self.CustomButton('Ocultar Over', self.main_window)
        self.ocultar_over_button.clicked.connect(lambda: self.mostrar_over(False))
        self.ocultar_over_button.setFixedHeight(50)
        self.ocultar_over_button.move(self.ancho - 110, 120)

        self.overlay_button = self.CustomButton('Overlay On/Off', self.main_window)
        self.overlay_button.clicked.connect(self.overlay_control)
        self.overlay_button.setMaximumHeight(20)
        self.overlay_button.move(10, 135)

        self.fondo_rojo_button = self.CustomButton('Fondo Rojo', self.main_window)
        self.fondo_rojo_button.clicked.connect(lambda: self.fondo_color('#FF0000'))
        self.fondo_rojo_button.setMaximumHeight(20)
        self.fondo_rojo_button.move(110, 120)

        self.fondo_verde_button = self.CustomButton('Fondo Verde', self.main_window)
        self.fondo_verde_button.clicked.connect(lambda: self.fondo_color('#00FF00'))
        self.fondo_verde_button.setMaximumHeight(20)
        self.fondo_verde_button.move(210, 120)

        self.fondo_azul_button = self.CustomButton('Fondo Azul', self.main_window)
        self.fondo_azul_button.clicked.connect(lambda: self.fondo_color('#0000FF'))
        self.fondo_azul_button.setMaximumHeight(20)
        self.fondo_azul_button.move(310, 120)

        self.fondo_blanco_button = self.CustomButton('Fondo Blanco', self.main_window)
        self.fondo_blanco_button.clicked.connect(lambda: self.fondo_color('#FFFFFF'))
        self.fondo_blanco_button.setMaximumHeight(20)
        self.fondo_blanco_button.move(110, 150)
        
        self.fondo_negro_button = self.CustomButton('Fondo Negro', self.main_window)
        self.fondo_negro_button.clicked.connect(lambda: self.fondo_color('#000000'))
        self.fondo_negro_button.setMaximumHeight(20)
        self.fondo_negro_button.move(210, 150)

        self.fondo_gris_button = self.CustomButton('Fondo Gris', self.main_window)
        self.fondo_gris_button.clicked.connect(lambda: self.fondo_color('#808080'))
        self.fondo_gris_button.setMaximumHeight(20)
        self.fondo_gris_button.move(310, 150)

        self.redibujar_circulo()
        self.mostrar_botones(False)

    def mostrar_botones(self,mostrar:bool):
        self.mostrar_ctrl(mostrar)
        self.mostrar_pen(mostrar)
        self.mostrar_over(mostrar)

    def mostrar_botones_control(self):
        if self.btnctrl_status:
            self.ustatus_btns_ctrl = self.status_btns_ctrl
            self.ustatus_btns_pen = self.status_btns_pen
            self.ustatus_btns_over = self.status_btns_over    
            self.mostrar_botones(False)
            self.mostrar_ctrl_button.setVisible(False)
            self.mostrar_pen_button.setVisible(False)
            self.mostrar_over_button.setVisible(False)
            self.ocultar_ctrl_button.setVisible(False)
            self.ocultar_pen_button.setVisible(False)
            self.ocultar_over_button.setVisible(False)
            self.btnctrl_status = False
        else:
            self.mostrar_ctrl(self.ustatus_btns_ctrl)
            self.mostrar_pen(self.ustatus_btns_pen)
            self.mostrar_over(self.ustatus_btns_over)
            self.btnctrl_status = True
    
    def mostrar_ctrl(self,mostrar:bool):
        self.status_btns_ctrl = mostrar
        self.ocultar_ctrl_button.setVisible(mostrar)
        self.minimize_button.setVisible(mostrar)
        self.maximize_button.setVisible(mostrar)
        self.restore_button.setVisible(mostrar)
        self.close_button.setVisible(mostrar)
        if not mostrar:
            self.mostrar_ctrl_button.setVisible(True)
        
    def mostrar_pen(self, mostrar:bool):
        self.logo_label.setVisible(mostrar)
        self.status_btns_pen = mostrar
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
        self.status_btns_over = mostrar
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
        if self.status_btns_pen: self.main_window.drawing_view.current_circle = self.main_window.drawing_view.scene().addEllipse(335, 48, 50, 50, self.main_window.drawing_view.pen)
    
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
            self.main_window.estilo_botones()
        
        