from PyQt5 import uic
from tkinter import *
import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView

from sorts.sort import Sort


class Main(QMainWindow):
    # Array principal para las dimensines de las barras
    barList = []
    lengthList = []
    worker = None

    numBars = 15
    w_width = 1024
    w_height = 600
    width_bar = w_width / numBars
    height_bar_base = w_height / numBars

    # Atributos para configuracion de la animacion
    selectAlgoritm = 'Optimized Bubble Sort'  # Valor por defecto

    def __init__(self):
        super().__init__()
        self.pen = QPen(QColor("#fff"))
        self.grayBrush = QBrush(QColor("#f2a"))
        self.greenBrush = QBrush(Qt.green)
        self.scene = QGraphicsScene()
        uic.loadUi('interface/ui_main.ui', self)
        self.initGenerate()

    def initGenerate(self):
        graphicView = QGraphicsView(self.scene, self)
        graphicView.setGeometry(290, 30, self.w_width, self.w_height)

        self.shapes()

    def shapes(self):
        # canvas.delete('all')
        i = 1
        for bar in range(self.numBars):
            x = self.width_bar * i
            y = 1000
            wb = self.width_bar
            hb = self.height_bar_base * i
            bar = self.scene.addRect(x, y, wb, hb, self.pen, self.grayBrush)
            self.barList.append(bar)
            i += 1


if __name__ == "__main__":
    # Instancia De la Clase Sort
    sort = Sort()

    app = QApplication(sys.argv)
    GUI = Main()
    GUI.show()
    sys.exit(app.exec_())
