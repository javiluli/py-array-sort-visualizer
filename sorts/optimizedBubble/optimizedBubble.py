import time

def optimizedBubble_sort(data, drawData=None, timeTick=0):
  n = len(data)

  for i in range(n):
    swapped = False

    for j in range(0, n-i-1):
      # swap values
      if data[j] > data[j+1]:
        data[j], data[j+1] = data[j+1], data[j]
        swapped = True

      # Dibujar datos
      if drawData != None: 
        drawData(data, ['#4682B4' if x == j + 1 else "#9370DB" for x in range(len(data))])

      # retardo
      time.sleep(timeTick)
    
    # si no ha hecho swap values
    if swapped == False:
      break

  if drawData != None:
    drawData(data, ['#4682B4' for x in range(len(data))])

  return data
    