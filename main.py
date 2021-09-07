from tkinter import *
from tkinter import ttk
import threading

# Algoritmos de ordenacion / sorts
from sorts.bubble.bubble import bubble_sort

# Importar clases
from classes.Configuracion import Configuracion
from classes.ArraySort import ArraySort

class MainProgram:

  # Array principal para las dimensines de las barras
  data = []

  # Atributos para configuracion de la animacion
  numBars = 16
  mostrarTextoBarras = False

  def __init__(self):
    self.root = Tk()
    self.root.title("Array sort visualizer")
    # self.root.geometry("950x600")
    self.root.geometry("{}x{}+{}+{}".format(950, 600, 200, 100))
    self.root.config(bg='black')
    self.root.resizable(0,0)
    self.agregar_menu()
    self.initGenerate()
    self.root.mainloop()

  def agregar_menu(self):
    """ 1. Menu principal superior """
    C_MENU = Canvas(self.root, width=950, height=50, bg='#f0f0f0', highlightthickness=0)
    C_MENU.grid(row=0, column=0)
    C_MENU.grid_propagate(False)
    C_MENU.grid_rowconfigure(0, weight=1)
    C_MENU.grid_columnconfigure(0, weight=1)

    # Frame para almacenar los botones de accion del programa
    F_MENU_BTNS = Frame(C_MENU, width=950, height=50, bg='#f0f0f0')
    F_MENU_BTNS.grid(row=0, column=0, sticky=W)

    # Col[0] - Button Play
    self.photoPlay = PhotoImage(file = r"./img/play-button.png")
    self.btnStart = Button(F_MENU_BTNS, text='play', width=26, height=26, bg="#f0f0f0", border=0, activebackground="#ffffff", command=self.startAlgorithm, image=self.photoPlay)
    self.btnStart.grid(row=0, column=0, padx=10, pady=0)
    # Col[1] - Button restart
    self.photoRefresh = PhotoImage(file = r"./img/refresh.png")
    self.btnRestart = Button(F_MENU_BTNS, text='restart', width=26, height=26, bg="#f0f0f0", border=0, activebackground="#ffffff", command=self.generate, image=self.photoRefresh)
    self.btnRestart.grid(row=0, column=1, padx=10, pady=0)
    # Col[2] - Button settings
    self.photoSettings = PhotoImage(file = r"./img/settings.png")
    self.btnSettings = Button(F_MENU_BTNS, text='settings', width=26, height=26, bg="#f0f0f0", border=0, activebackground="#ffffff", command=self.openSettings, image=self.photoSettings)
    self.btnSettings.grid(row=0, column=2, padx=10, pady=0)

    """ 2. Canvas para la representacion de las barras del array y animaciones """
    C_BODY = Canvas(self.root, width=950, height=550, bg='#ffffff', highlightthickness=0)
    C_BODY.grid(row=1, column=0)
    C_BODY.grid_propagate(False)

    # Canvas que rodea el Canvas principal con la animacion del algoritmo Sort
    C_BODY_BORDER = Canvas(C_BODY, width=900, height=500, bg='#ffffff', bd=-2)
    C_BODY_BORDER.create_rectangle(0, 0, 900, 500, width=2)
    C_BODY_BORDER.grid(row=0, column=0, padx=20, pady=20)

    # Canvas principal donde se representa el array y su animacion de ordenacion
    self.C_BODY_ANIMATION = Canvas(C_BODY, width=860, height=460, bg='#ffffff', bd=-2)
    self.C_BODY_ANIMATION.grid(row=0, column=0, padx=20, pady=20)

  def drawData(self, data, colorArray):
    self.C_BODY_ANIMATION.delete('all')
    c_height = 460
    c_widtht = 860
    x_widtht = c_widtht / len(data)
    offset = 0
    spacing = 0
    normalizeData = [i / max(data) for i in data]
    for i, height in enumerate(normalizeData):
      # top left
      x0 = i * x_widtht + offset + spacing
      y0 = c_height - height * 440
      # bottom right
      x1 = (i + 1) * x_widtht + offset
      y1 = c_height
      self.C_BODY_ANIMATION.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="")
      # Texto sobre las barras
      if (self.mostrarTextoBarras):
        self.C_BODY_ANIMATION.create_text((x0 + 2), y0, anchor=SW, text=str(data[i]))
    self.root.update_idletasks()

  def generate(self):
    self.data = arraySort.shuffleArray(self.data, self.numBars)
    self.drawData(self.data, ['#9370DB' for x in range(len(self.data))])

  def startAlgorithm(self):
    bubble_sort(self.data, self.drawData, 0.01)

  def initGenerate(self):
    self.data = arraySort.initArray(self.data, self.numBars)
    self.drawData(self.data, ['#9370DB' for x in range(len(self.data))])

  def openSettings(self):
    settings=Configuracion(self.root)
    dataSettings=settings.obtenerConfiguracion()
    self.numBars = dataSettings[0]
    self.mostrarTextoBarras = dataSettings[1]
    self.initGenerate()

if __name__ == '__main__':
  # Instancia De la Clase ArraySort
  arraySort = ArraySort()
  # Main loop
  main=MainProgram()
