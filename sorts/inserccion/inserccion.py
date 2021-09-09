import time

def inserccion_sort(data, drawData=None, timeTick=0):
  n = len(data)

  for i in range(n):
    pos = i
    aux = data[i]

    while pos > 0 and data[pos - 1] > aux:
      data[pos] = data[pos - 1]
      pos-=1
      data[pos] = aux

      # Dibujar datos
      if drawData != None: 
        drawData(data, ['#4682B4' if x == i + 1 else "#9370DB" for x in range(len(data))])
        
      # retardo
      time.sleep(timeTick)
      
  return data
