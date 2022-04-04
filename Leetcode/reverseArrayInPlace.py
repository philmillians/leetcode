class Solution:
  def reverseArrayInPlace(self, array):
    start=0
    end = len(array)-1
    while start < end:
      array[start], array[end] = array[end] , array[start]
      start += 1
      end -= 1
    return array
