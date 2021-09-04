from tkinter import *
from tkinter import ttk
import random
from sorts.bubble.bubble import bubble_sort

root = Tk()
root.title("Array sort visualizer")
root.geometry("950x600")
root.config(bg='black')

# variables
selected_alg = StringVar()
data = []
MIN_BAR = 2
MAX_BAR = 2**5

def initArrayData(maxBar):
    global data

    data = []
    for x in range(maxBar):
        data.append(x+1) 

def drawData(data, colorArray):
    C_BODY_ANIMATION.delete('all')
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
        C_BODY_ANIMATION.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="")
        C_BODY_ANIMATION.create_text(x0 + (x_widtht/2) - 6, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


def Generate():
    global data
    global MAX_BAR

    initArrayData(MAX_BAR)

    for x in range(MAX_BAR):
        rng = random.randrange(0, MAX_BAR)
        data[x], data[rng] = data[rng], data[x] 
    drawData(data, ['steelblue' for x in range(len(data))])

def StartAlgorithm():
    global data
    bubble_sort(data, drawData, 0.01)

def initGenerate():
    global data 
    initArrayData(MAX_BAR)
    drawData(data, ['steelblue' for x in range(len(data))])

def openSettings():
    settingWindows = Toplevel()
    settingWindows.grab_set() # Mantiene el foco de la ventana hasta que se cierre y devuelve la interacción con la ventana principal, el root en este caso.
    settingWindows.focus_set() # Mantiene el foco cuando se abre la ventana.
    settingWindows.title("Opciones")
    settingWindows.geometry("600x400")
    settingWindows.config(bg='white')

    sizeEntry = Scale(settingWindows, from_=3, to=25, resolution=1, orient=HORIZONTAL, label='Data size')
    sizeEntry.grid(row=1, column=0, padx=5, pady=5)

    minEntry = Scale(settingWindows, from_=0, to=10, resolution=1, orient=HORIZONTAL, label='Min value')
    minEntry.grid(row=1, column=1, padx=5, pady=5)

    maxEntry = Scale(settingWindows, from_=10, to=100, resolution=1, orient=HORIZONTAL, label='Max value')
    maxEntry.grid(row=1, column=2, padx=5, pady=5)

    speedScale = Scale(settingWindows, from_=0.1, to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label="Select Speed [s]")
    speedScale.grid(row=0, column=2, padx=5, pady=5)

"""Menu principal superior"""
C_MENU = Canvas(root, width=950, height=50, bg='#f0f0f0', highlightthickness=0)
C_MENU.grid(row=0, column=0)
C_MENU.grid_propagate(False)
C_MENU.grid_rowconfigure(0, weight=1)
C_MENU.grid_columnconfigure(0, weight=1)

# Frame para almacenar los botones de accion del programa
F_MENU_BTNS = Frame(C_MENU, width=950, height=50, bg='#f0f0f0')
F_MENU_BTNS.grid(row=0, column=0, sticky=W)

# Col[0] - Button Play
photoPlayButton = PhotoImage(file = r"./img/play-button.png")
Button(F_MENU_BTNS, text='play', width=26, height=26, bg="#f0f0f0", border=0, activebackground="#ffffff", command=StartAlgorithm, image=photoPlayButton).grid(row=0, column=0, padx=5, pady=5)
# Col[1] - Button restart
photoRefresh = PhotoImage(file = r"./img/refresh.png")
Button(F_MENU_BTNS, text='restart', width=26, height=26, bg="#f0f0f0", border=0, activebackground="#ffffff", command=Generate, image=photoRefresh).grid(row=0, column=1, padx=5, pady=5)
# Col[2] - Button settings
# photoSettings = PhotoImage(file = r"./img/settings.png")
# Button(F_MENU_BTNS, text='settings', width=26, height=26, bg="#f0f0f0", border=0, activebackground="#ffffff", command=openSettings, image=photoSettings).grid(row=0, column=2, padx=5, pady=5)

"""Canvas para la representacion de las barras del array y animaciones"""
C_BODY = Canvas(root, width=950, height=550, bg='#ffffff', highlightthickness=0)
C_BODY.grid(row=1, column=0)
C_BODY.grid_propagate(False)

# Canvas que rodea el Canvas principal con la animacion del algoritmo Sort
C_BODY_BORDER = Canvas(C_BODY, width=900, height=500, bg='#ffffff', bd=-2)
C_BODY_BORDER.create_rectangle(0, 0, 900, 500, width=2)
C_BODY_BORDER.grid(row=0, column=0, padx=20, pady=20)

# Canvas principal donde se representa el array y su animacion de ordenacion
C_BODY_ANIMATION = Canvas(C_BODY, width=860, height=460, bg='#ffffff', bd=-2)
C_BODY_ANIMATION.grid(row=0, column=0, padx=20, pady=20)

# Iniciado de animaciones al iniciar el programa
initGenerate()

# Main loop
root.mainloop()
