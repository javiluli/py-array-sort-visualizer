import tkinter as tk
from tkinter import *
from tkinter import ttk
from sorts.sort import Sort


class MainProgram:
  worker = None
  delay = 10
  
  # Medidas de la ventana root
  root_w_width = 1350
  root_w_height = 665

  LIST_ALGORITHM = [
    'Bubble Sort',
    'Optimized Bubble Sort',
    'Insertion Sort',
    'Selection Sort'
  ]

  def __init__(self):
    self.root = Tk()
    self.root.title("Array sort visualizer")
    self.root.geometry("{}x{}+{}+{}".format(self.root_w_width, self.root_w_height, 200, 100))
    self.root.config(bg='black')
    self.root.resizable(0, 0)
    self.agregar_menu()
    self.generate()
    self.root.mainloop()

  def agregar_menu(self):
    """ 1. Menu principal superior """
    C_MENU = Canvas(self.root, width=280, height=665, bg='#ffffff', highlightthickness=0)
    C_MENU.grid(row=0, column=0)
    C_MENU.grid_propagate(False)

    # Selecctor de algoritmo de ordenacion
    self.selected_alg = tk.StringVar()
    self.algoritmSelection = ttk.Combobox(C_MENU, textvariable=self.selected_alg, values=self.LIST_ALGORITHM)
    self.algoritmSelection.current(0)
    self.algoritmSelection.place(x=20, y=30)

    # Button Play
    self.btnStart = Button(C_MENU, text='Iniciar', bg="#f0f0f0", border=0, activebackground="#ffffff",
                           command=self.startAlgorithm)
    self.btnStart.place(x=20, y=70)

    # Button restart
    self.btnRestart = Button(C_MENU, text='Desordenar', bg="#f0f0f0", border=0, activebackground="#ffffff",
                             command=self.shuffleBars)
    self.btnRestart.place(x=70, y=70)
    self.btnRestart

    # Input para la cantidad de barras en el array y su animacion
    self.labelNumbars = Label(C_MENU, text="Cantidad de barras", bg="#ffffff")
    self.labelNumbars.place(x=20, y=120)
    self.numBarsSlide = tk.IntVar()
    self.entryNumBars = tk.Scale(C_MENU, from_=(2 ** 1), to=(2 ** 10), bg="#ffffff", length=240, resolution=1, orient=HORIZONTAL, variable=self.numBarsSlide)
    self.entryNumBars.place(x=20, y=150)
    self.numBarsSlide.set(32)

    # Input para la cantidad de barras en el array y su animacion
    self.labelDelay = Label(C_MENU, text="Delay en la animacion (segundos)", bg="#ffffff")
    self.labelDelay.place(x=20, y=200)
    self.timeSlide = tk.IntVar()
    self.entrytimeSlide = tk.Scale(C_MENU, from_=1, to=100, length=240, resolution=1, orient=HORIZONTAL, variable=self.timeSlide)
    self.entrytimeSlide.place(x=20, y=230)

    # Button config
    self.btnConfig = Button(C_MENU, text='Aplicar cambios', bg="#f0f0f0", border=0, activebackground="#ffffff", command=self.config)
    self.btnConfig.place(x=20, y=290)
    self.btnConfig

    """ 2. Canvas para la representacion de las barras del array y animaciones """
    C_BODY = Canvas(self.root, width=1070, height=665, bg='#ffffff', highlightthickness=0)
    C_BODY.grid(row=0, column=1)
    C_BODY.grid_propagate(False)

    # Canvas que rodea el Canvas principal con la animacion del algoritmo Sort
    C_BODY_BORDER = Canvas(C_BODY, width=1060, height=645, bg='#ffffff', bd=-2)
    C_BODY_BORDER.create_rectangle(0, 0, 1060, 645, width=2)
    C_BODY_BORDER.grid(row=0, column=0, pady="10")

    # Canvas principal donde se representa el array y su animacion de ordenacion
    self.C_BODY_ANIMATION = Canvas(C_BODY, width=1024, height=600, bg='#ffffff', bd=-2)
    self.C_BODY_ANIMATION.grid(row=0, column=0, padx=20, pady=20)

  # Animation Function
  def animate(self):
    if self.worker is not None:
      try:
        next(self.worker)
        self.root.after(self.delay, self.animate)
      except StopIteration:
        self.worker = None
      finally:
        self.root.after_cancel(self.animate)

  def shuffleBars(self):
    self.worker = sort.shuffle(self.C_BODY_ANIMATION)
    self.animate()

  def startAlgorithm(self):
    def __bubble():
      self.worker = sort.bubble_sort(self.C_BODY_ANIMATION)

    def __optimizedBubble():
      self.worker = sort.optimizedBubble_sort(self.C_BODY_ANIMATION)

    def __insertion():
      self.worker = sort.insertion_sort(self.C_BODY_ANIMATION)

    def __selection():
      self.worker = sort.selection_sort(self.C_BODY_ANIMATION)

    select_algorithm = {
      0: __bubble,
      1: __optimizedBubble,
      2: __insertion,
      3: __selection,
    }
    algorithm = self.algoritmSelection.current()
    select_algorithm.get(algorithm)()
    self.animate()

  def generate(self):
    sort.drawGraphics(self.C_BODY_ANIMATION)

  def config(self):
    # Tiempo de retardo en la animacion
    self.delay = self.entrytimeSlide.get()
    # Configuracion de las barras
    sort.barList = []
    sort.lengthList = []
    sort.numBars = self.entryNumBars.get()
    sort.width_bar = sort.w_width / sort.numBars
    sort.height_bar_base = sort.w_height / sort.numBars
    # iniciar animacion
    self.generate()


if __name__ == '__main__':
  # Instancia De la Clase Sort
  sort = Sort()
  # Main loop
  main = MainProgram()
