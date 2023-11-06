#!UTC/Encode to Python with Monkey Python Coddebuging Circus by Alan.R.G.Systemas c.2023¡#
'''
OverDraw by Alan.R.G.Systemas now tested on Xubuntu 20.04.6 LTS with enable display compositing (Nov-2023)

Documentación y Control de Versionado
v.0.8.5 (05/11/2023 Día cinco, pensaba agregar una figura de fibonacci, pero me di cuenta que habia
un error en la determinacion del lienzo del dibujo en el mainwindow, lo que ocacionó una serie de
pruebas y errores que me hicieron perder mucho tiempo, tengo un bug en la zona suerior izquierda,
no sé que es, la IA tampoco, y ya estoy cansado. lo dejo por hoy.
# se soluciona problema de doble lienzo en la ventana principal.

v.0.8.4 (31/10/2023) Día cuatro, hoy me dí cuenta que Bard es mucho mas inteligente como inteligencia
artificial que la estupidez artificial de ChatGPT 3.5, no sólo recordó lo que hablamos anoche, sino
que me ayudo proporcionando partes de código sin errores para diferentes funciones.
# Se agrega la posibilidad de seleccionar el shape elipse y trazarlas.
# Se agrega en hoja de estilos de la toolbar elementos de estilo para los cuadros de dialogo.
# Se corrige la logica de seleccion de estilos para el modo overlay.
# Se implementa código para trazar los diferentes shapes.
# Se debuguean errores de logica general y metodos entre clases.

v.0.8.3 (30/10/2023) Día tres, es tres, estres, mucho estres... cansado de luchar con un mouse que
se mueve bien pero que falla el clic y hace doble clic solo, o se suelta el clic solo, que es lo mismo,
pero no, pero no es lo mismo, pero molesta y muchisimo...
cambié de mouse antes de volverme más loco que antes de volverme muy loco. Voy a guardar un backup 
antes que un mouse que ande mal me borre todo... ahhhhhhhhh.
# Se agrega boton para cuadro de dialogo seleccion de grosor de trazo.
# Se agregan botones de seleccion de shape (Lápiz, Línea, Rectángulo).
# Se implementa clase con cuadro de dialogo para seleccion de shape.
# Se agrega boton al toolbar para seleccion de shape.
# Se agranda toolbar.
# Se colocan Iconos personalizados.
# Se coloca un separador entre iconos de toolbar que confguran el trazo y el icono de borrado.

v.0.8.2 (29/10/2023) Día dos, ayer fue el cumpleaños de mi hija, hoy Checo Perez chocó en la primer curva del
gran premi de Mexico, lo unico que pude hacer fue con la limitada inteligencia artificial de chatGPT 
3.5 probar los diferentes metodos de Qpen, pero finalmente tuve que resolver solo muchas cosas básicas
me estoy empezando a cansar de la estupidez artificial, espero que esto no me haga odiar a los 
programadores y mucho menos programar que es una gran forma de divertirse.
# Se Agregua Qt.RoundCap a Qpen para que escriba las lindo.
# Se agrega ventana de dialogo de selección de color desde paleta de colores o personalizado.
# Se agrega ventana de dialogo de selección de grosor de trazo.
# Se implementa la clase menu_handler.py para agregar una barra de menu
# Se implementa la clase toolbar_handler.py para agregar una barra de herramientas flotante.

v.0.8.1 (27/10/2023) Día uno, el código se muestra esquivo como las ballenas en los mares de hoy en día,
hubiera preferido que la IA me recomendara mejores sintaxis, o al menos, con muchos menos errores...
sin embargo, y a pesar de las diferencias que tuvimos otrora tiempo, entendí que las peores enemigas
son las espectativas, entonces, lejos de esperar soluciones milagrosas, me dedico y dediqué el día
de hoy a resolver entre otras cosas lo siguiente:
# Transparencia de la ventana de dibujo DrawingOverlay.
# Adaptación automática de tamaño del DrawingOverlay en función del tamaño de MainWindow.
# Organización general del programa.
# Separación de las clases según su función.
# Diseño de interfaz clara y minimalista.
# Posibilidad de ocultar los botones de cada control y ejemplo de trazo una vez configurado a gusto.
# Implementación de las funciones básicas de dibujo a mano alzada, a saber:
Grosor de trazo (y su memoría)
Ejemplo em pantalla de dicho Grozor
Color del trazo (y su memoría)
Borrado de pantalla
Color de fondo (y su memoría)
'''
import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())