import colorsys
import random

class Sort:
  barList = []  # Obj canvas
  lengthList = []  # coords Obj canvas
  numBars = 32
  w_width = 1024
  w_height = 600
  width_bar = w_width / numBars
  height_bar_base = w_height / numBars

  def __init__(self):
    pass

  def hsl2rgb(self, h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

  def rgb2hex(self, color):
    return '#%02x%02x%02x' % color

  def toDecimal(self, number):
    return round((255 / number), 10)

  def drawGraphics(self, canvas):
    canvas.delete('all')
    i = 0
    for bar in range(self.numBars):
      # set rainbow color
      decimal = round((self.toDecimal(self.numBars) * i), 10)
      parentage = round(decimal / 255 * 100 / 100, 3)
      rgb_color = self.hsl2rgb(parentage, 1, 1)

      # top left
      x0 = self.width_bar * i
      y0 = self.w_height - (self.height_bar_base * i) - self.height_bar_base
      # bottom right
      x1 = self.width_bar * (i + 1)
      y1 = self.w_height

      # set canvas rectangle
      bar = canvas.create_rectangle(x0, y0, x1, y1, fill=self.rgb2hex(rgb_color), outline="")
      self.barList.append(bar)
      i += 1

    # Getting length of the bar and appending into length list
    for bar in self.barList:
      bar = canvas.coords(bar)
      length = bar[3] - bar[1]
      self.lengthList.append(length)

  # cambio de coordenadas entre dos canvas
  def swapCoords(self, pos_0, pos_1, canvas):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21 - bar11, 0)
    canvas.move(pos_1, bar12 - bar22, 0)

  def shuffle(self, canvas):
    for i in range(len(self.lengthList)):
      rng = random.randrange(0, self.numBars)
      self.lengthList[i], self.lengthList[rng] = self.lengthList[rng], self.lengthList[i]
      self.barList[i], self.barList[rng] = self.barList[rng], self.barList[i]
      self.swapCoords(self.barList[rng], self.barList[i], canvas)
      yield

  """ Bubble Sort """
  def bubble_sort(self, canvas):
    for i in range(len(self.lengthList) - 1):
      for j in range(len(self.lengthList) - i - 1):
        if self.lengthList[j] > self.lengthList[j + 1]:
          self.lengthList[j], self.lengthList[j + 1] = self.lengthList[j + 1], self.lengthList[j]
          self.barList[j], self.barList[j + 1] = self.barList[j + 1], self.barList[j]
          self.swapCoords(self.barList[j + 1], self.barList[j], canvas)
          yield

  """ Optimized Bubble Sort """
  def optimizedBubble_sort(self, canvas):
    n = len(self.lengthList)
    for i in range(n):
      swapped = False
      for j in range(n - i - 1):
        # swap values
        if self.lengthList[j] > self.lengthList[j + 1]:
          self.lengthList[j], self.lengthList[j + 1] = self.lengthList[j + 1], self.lengthList[j]
          self.barList[j], self.barList[j + 1] = self.barList[j + 1], self.barList[j]
          self.swapCoords(self.barList[j + 1], self.barList[j], canvas)
          swapped = True
          yield
      # si no ha hecho swap values
      if not swapped:
        break

  """ Insertion Sort """
  def insertion_sort(self, canvas):
    for i in range(len(self.lengthList)):
      cursor = self.lengthList[i]
      cursorBar = self.barList[i]
      pos = i
      while pos > 0 and self.lengthList[pos - 1] > cursor:
        self.lengthList[pos] = self.lengthList[pos - 1]
        self.barList[pos], self.barList[pos - 1] = self.barList[pos - 1], self.barList[pos]
        self.swapCoords(self.barList[pos], self.barList[pos - 1], canvas)
        yield
        pos -= 1
      self.lengthList[pos] = cursor
      self.barList[pos] = cursorBar
      self.swapCoords(self.barList[pos], cursorBar, canvas)
      yield
      
  """ Selection Sort """
  def selection_sort(self, canvas):
    # Traverse through all array elements
    for i in range(len(self.lengthList)):
      MIN_IDX = i
      for j in range(i + 1, len(self.lengthList)):
        if self.lengthList[MIN_IDX] > self.lengthList[j]:
          MIN_IDX = j
      self.lengthList[i], self.lengthList[MIN_IDX] = self.lengthList[MIN_IDX], self.lengthList[i]
      self.barList[i], self.barList[MIN_IDX] = self.barList[MIN_IDX], self.barList[i]
      self.swapCoords(self.barList[MIN_IDX], self.barList[i], canvas)
      yield
