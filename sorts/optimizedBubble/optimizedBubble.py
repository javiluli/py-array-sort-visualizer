# from sorts.sort import Sort

# class OptimizedBubble(Sort):

#   def __init__(self):
#     pass

#   def optimizedBubble_sort(self, canvas):

#     n = len(self.lengthList)
    
#     for i in range(n):
#       swapped = False

#       for j in range(n - i - 1):
        
#         # swap values
#         if self.lengthList[j] > self.lengthList[j + 1]:
#           self.lengthList[j], self.lengthList[j + 1] = self.lengthList[j + 1], self.lengthList[j]

#           self.barList[j], self.barList[j + 1] = self.barList[j + 1], self.barList[j]

#           self.swapCoords(self.barList[j + 1], self.barList[j], canvas)

#           swapped = True
          
#           yield

#       # si no ha hecho swap values
#       if not swapped:
#         break
