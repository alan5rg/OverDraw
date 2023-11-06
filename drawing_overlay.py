from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtCore import Qt

class DrawingOverlay(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent
        self.pen = QPen(QColor(0, 255, 0), 5.0, Qt.SolidLine, Qt.RoundCap)
        self.last_pos = None
        self.shapes = ["Lápiz","Línea","Rectángulo","Elipse"]
        self.select_shape = self.shapes[0]
        self.current_circle = None
        self.tamanio = self.frameSize()
        self.ancho = self.tamanio.width()
        self.alto = self.tamanio.height()
        self.drawing_UI()

    def drawing_UI(self):
        # Antialiasing (no usar lo hace lento y no mejora significativamente nada)
        #self.setRenderHint(QPainter.Antialiasing)
        #self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        #self.setOptimizationFlag(QGraphicsView.DontAdjustForAntialiasing, True)
        #self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.setScene(QGraphicsScene(self))
        self.setSceneRect(0, 0, self.ancho, self.alto)
        
        # Configurar el fondo transparente
        self.setStyleSheet("background: transparent;")
        self.setAttribute(Qt.WA_AlwaysStackOnTop)

    def mousePressEvent(self, event):
        self.press_pos = event.pos()
        if self.select_shape == "Línea":
            # Inicia una nueva línea
            self.current_shape = self.scene().addLine(self.press_pos.x(), self.press_pos.y(), self.press_pos.x(), self.press_pos.y(), self.pen)
        if self.select_shape == "Rectángulo":
            # Inicia un nuevo rectángulo
            self.current_shape = self.scene().addRect(self.press_pos.x(), self.press_pos.y(), 0, 0, self.pen)
        if self.select_shape == "Elipse":
            # Inicia un nuevo círculo
            self.current_shape = self.scene().addEllipse(self.press_pos.x(), self.press_pos.y(), 0, 0, self.pen)

    def mouseMoveEvent(self, event):
        self.current_pos = event.pos()
        if self.last_pos is not None and self.select_shape is not None:
            if self.select_shape == "Lápiz":
                self.scene().addLine(self.last_pos.x(), self.last_pos.y(), self.current_pos.x(), self.current_pos.y(), self.pen)
            if self.select_shape == "Línea":
                # Actualiza el tamaño de la linea
                self.current_shape.setLine(self.press_pos.x(), self.press_pos.y(), event.pos().x(), event.pos().y())
            if self.select_shape == "Rectángulo":
                # Actualiza el tamaño del rectángulo
                self.current_shape.setRect(self.press_pos.x(), self.press_pos.y(), self.current_pos.x() - self.press_pos.x(), self.current_pos.y() - self.press_pos.y())
            if self.select_shape == "Elipse":
                # Actualiza el tamaño del círculo
                self.current_shape.setRect(self.press_pos.x(), self.press_pos.y(), self.current_pos.x() - self.press_pos.x(), self.current_pos.y() - self.press_pos.y())
        self.last_pos = self.current_pos

    def mouseReleaseEvent(self, event):
        self.rele_pos = event.pos()
        if self.select_shape == "Línea":
            # Finaliza la forma línea y la hace permanente
            self.scene().addLine(self.press_pos.x(), self.press_pos.y(), self.rele_pos.x(), self.rele_pos.y(), self.pen)
        if self.select_shape == "Rectángulo":
            # Finaliza el rectángulo y lo hace permanente
            self.scene().addRect(self.press_pos.x(), self.press_pos.y(), self.rele_pos.x() - self.press_pos.x(), self.rele_pos.y() - self.press_pos.y(), self.pen)
        if self.select_shape == "Elipse":
            # Finaliza el círculo y lo hace permanente
            self.scene().addEllipse(self.press_pos.x(), self.press_pos.y(), self.rele_pos.x() - self.press_pos.x(), self.rele_pos.y() - self.press_pos.y(), self.pen)
        self.press_pos = None
        self.last_pos = None
        self.rele_pos = None

    def resizeEvent(self, event):
        new_size = event.size()
        #se utilizan las variables globales de ancho y alto
        self.ancho = new_size.width() 
        self.alto = new_size.height()
        self.setSceneRect(0, 0, self.ancho, self.alto)