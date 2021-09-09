import time

def bubble_sort(data, drawData=None, timeTick=0):
  for i in range(len(data)):

    for j in range(len(data) - 1):

      if data[j] > data[j+1]:
        data[j], data[j+1] = data[j+1], data[j]

      if drawData != None: 
        drawData(data, ['#4682B4' if x == j + 1 else "#9370DB" for x in range(len(data))])

      time.sleep(timeTick)

  if drawData != None:
    drawData(data, ['#4682B4' for x in range(len(data))])

  return data
