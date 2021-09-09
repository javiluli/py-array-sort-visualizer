import tkinter as tk
from tkinter import ttk
from tkinter import *

class Configuracion:

  def __init__(self, ventanaPrincipal):
    # VEntana Toplevel emergente
    self.settings = Toplevel(ventanaPrincipal)
    self.settings.title('Opciones')
    self.settings.geometry("{}x{}+{}+{}".format(600, 350, 220, 200))
    self.settings.config(bg='white')

    # Input para la cantidad de barras en el array y su animacion
    self.numBarsSlide=tk.IntVar()
    self.entryNumBars=tk.Scale(self.settings, from_=(2**1), to=(2**8), length=580, resolution=1, sliderlength=15, takefocus=34, orient=HORIZONTAL, label='Data size', variable=self.numBarsSlide)
    self.entryNumBars.grid(row=0, column=0, padx=5, pady=5)

    # Input para el tiempo de delay
    self.timeSlide=tk.IntVar()
    self.entrytimeSlide=tk.Scale(self.settings, from_=0.001, to=0.1, length=580, resolution=0.001, sliderlength=30, orient=HORIZONTAL, label='Time', variable=self.timeSlide)
    self.entrytimeSlide.grid(row=1, column=0, padx=5, pady=5)

    # Checkbox para mostrar el valor de las barras sobre las mismas
    self.mostrarTexto = tk.IntVar()
    self.btnMostrarTexto = Checkbutton(self.settings, text='Mostrar valor de las barras', variable = self.mostrarTexto, onvalue = 1, offvalue = 0,)
    self.btnMostrarTexto.grid(row=2, column=0, padx=10, pady=0, sticky=W)

    # Selecctor de algoritmo de ordenacion
    self.selected_alg =tk.StringVar()
    self.algoritmSelection = ttk.Combobox(self.settings, textvariable=self.selected_alg, 
      values=
      [
        'Bubble Sort', 
        'Optimized Bubble Sort', 
        'Inserccion Sort', 
        'Selection Sort'
      ]
    )
    self.algoritmSelection.grid(row=3, column=0, padx=5, pady=5,  sticky=W)
    self.algoritmSelection.current(0)

    # Buton que aplica los cambios en funcion de los valores de los inputs anteriores
    self.btnAplicar = Button(self.settings, text='Aplicar', command=self.aplicarSettings)
    self.btnAplicar.grid(row=4, column=0, padx=10, pady=0, sticky=W)

  """Obtener la configuracion para mostrar el Array Sort

  Return:
    [Tupla] - Datos obtenido para la configuracion de la animacion
  """
  def obtenerConfiguracion(self):
    self.settings.wait_window()
    # [0]
    numBarsSlide = self.numBarsSlide.get()
    # [1]
    timeSlide = self.timeSlide.get()
    # [2]
    mostrarTexto = self.isChecked(self.mostrarTexto.get())
    # [3]
    selectedAlg = self.selected_alg.get()

    return (numBarsSlide, timeSlide, mostrarTexto, selectedAlg)

  """Saber si un input de tipo checkbos esta activo o no

  Return:
    [Boolean] - True si esta marcado, False si no esta marcado
  """
  def isChecked(self, value):
    if (value == 1): return True
    elif (value == 0): return False

  """Aplica los cambios y cierra la ventana Toplevel()
  """
  def aplicarSettings(self):
    self.settings.destroy()
