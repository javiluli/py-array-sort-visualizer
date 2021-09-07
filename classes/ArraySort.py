import random

class ArraySort:
  def __init__(self):
    pass

  def initArray(self, data, numBars):
    data = []
    for x in range(numBars):
        data.append(x+1)
    return data

  def shuffleArray(self, data, numBars):
    for x in range(numBars):
      rng = random.randrange(0, numBars)
      data[x], data[rng] = data[rng], data[x]
    return data
