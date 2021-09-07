from tkinter import *
import tkinter as tk

class Configuracion:

  def __init__(self, ventanaPrincipal):
    self.settings = Toplevel(ventanaPrincipal)
    self.settings.title("Opciones")
    self.settings.geometry("{}x{}+{}+{}".format(600, 350, 220, 200))
    self.settings.config(bg='white')

    self.numBarsSlide=tk.StringVar()
    self.entryNumBars=tk.Scale(self.settings, from_=(2**1), to=(2**8), length=580, resolution=1, sliderlength=15, takefocus=34, orient=HORIZONTAL, label='Data size', variable=self.numBarsSlide)
    self.entryNumBars.grid(row=0, column=0, padx=5, pady=5)

    self.mostrarTexto = tk.IntVar()
    self.btnMostrarTexto = Checkbutton(self.settings, text="Mostrar valor de las barras", variable = self.mostrarTexto, onvalue = 1, offvalue = 0,)
    self.btnMostrarTexto.grid(row=1, column=0, padx=10, pady=0, sticky=W)

    self.btnAplicar = Button(self.settings, text='Aplicar', command=self.aplicarSettings)
    self.btnAplicar.grid(row=2, column=0, padx=10, pady=0, sticky=W)

  """Obtener la configuracion para mostrar el Array Sort

  Return:
    [Tupla] - Datos obtenido para la configuracion de la animacion
  """
  def obtenerConfiguracion(self):
    self.settings.wait_window()
    # [0]
    numBarsSlide = int(self.numBarsSlide.get())
    # [1]
    mostrarTexto = self.isChecked(self.mostrarTexto.get())
    return (numBarsSlide, mostrarTexto)

  def isChecked(self, value):
    if (value == 1): return True
    elif (value == 0): return False

  def aplicarSettings(self):
    self.settings.destroy()
