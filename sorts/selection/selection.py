import time

def selection_sort(data, drawData=None, timeTick=0):
  n = len(data)

  for i in range(n):
    min = i
    j = i + 1

    for j in range(n):
      if (data[j] > data[min]):
        min = j

      data[i], data[min] = data[min], data[i]

    # Dibujar datos
    if drawData != None: 
      drawData(data, ['#4682B4' if x == i + 1 else "#9370DB" for x in range(len(data))])

    # retardo
    time.sleep(timeTick)

  if drawData != None:
    drawData(data, ['#4682B4' for x in range(len(data))])

  return data
