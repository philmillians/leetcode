class Solution:
    def replaceElements(self, arr):
      if len(arr) == 1:
        arr[0] = -1
      for i in range(0,len(arr)-1):
        slicedArray = arr[i+1:len(arr)]
        maxToRight = max(slicedArray)
        arr[i]=maxToRight
      arr[len(arr)-1]=-1
      return arr
