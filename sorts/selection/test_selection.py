import unittest
from selection import selection_sort

class TestSelectionSort(unittest.TestCase):
  data = [2, 7, 0, 1, 9, 6, 8, 3, 4, 5]

  def test_1(self):
    array = selection_sort(self.data)
    self.assertEqual(array, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
