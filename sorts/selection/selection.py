# import time

# from sorts.sort import Sort


# class Selection(Sort):

#   def __init__(self):
#     pass

#   def selection_sort(self, canvas):
#     # Traverse through all array elements
#     for i in range(len(self.lengthList)):

#       MIN_IDX = i
#       for j in range(i + 1, len(self.lengthList)):
#         if self.lengthList[MIN_IDX] > self.lengthList[j]:
#           MIN_IDX = j

#       self.lengthList[i], self.lengthList[MIN_IDX] = self.lengthList[MIN_IDX], self.lengthList[i]

#       self.barList[i], self.barList[MIN_IDX] = self.barList[MIN_IDX], self.barList[i]

#       self.swapCoords(self.barList[MIN_IDX], self.barList[i], canvas)

#       yield
