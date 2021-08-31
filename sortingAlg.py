from tkinter import *
from tkinter import ttk
import random
from sorts.bubble.bubble import bubble_sort

root = Tk()
root.title("Array sort visualizer")
root.maxsize(900, 600)
root.config(bg='black')

data = []

# variables
selected_alg = StringVar()

def drawData(data, colorArray):
    canvas.delete('all')
    c_height = 300
    c_widtht = 600
    x_widtht = c_widtht / (len(data) + 1)
    offset = 30
    spacing = 3
    normalizeData = [i / max(data) for i in data]
    for i, height in enumerate(normalizeData):
        # top left
        x0 = i * x_widtht + offset + spacing
        y0 = c_height - height * 260
        # bottom right
        x1 = (i + 1) * x_widtht + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))

    drawData(data, ['steelblue' for x in range(len(data))])


def StartAlgorithm():
    global data
    bubble_sort(data, drawData, speedScale.get())


# frame / base layout
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=300, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User interface area
# Row[0]
Label(UI_frame, text='Algoritmos: ', bg='grey',).grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text='Start', command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

# Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label='Data size')
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label='Min value')
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label='Max value')
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text='Generate', command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

# Main loop
root.mainloop()
