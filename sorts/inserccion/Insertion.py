# from sorts.sort import Sort


# class Insertion(Sort):
#   def __init__(self):
#     pass

#   def insertion_sort(self, canvas):

#     for i in range(len(self.lengthList)):
#       cursor = self.lengthList[i]
#       cursorBar = self.barList[i]
#       pos = i

#       while pos > 0 and self.lengthList[pos - 1] > cursor:
#         self.lengthList[pos] = self.lengthList[pos-1]
#         self.barList[pos], self.barList[pos - 1] = self.barList[pos - 1], self.barList[pos]
#         self.swapCoords(self.barList[pos], self.barList[pos - 1], canvas)
#         yield
#         pos -= 1

#       self.lengthList[pos] = cursor
#       self.barList[pos] = cursorBar
#       self.swapCoords(self.barList[pos], cursorBar, canvas)
      
#       yield
