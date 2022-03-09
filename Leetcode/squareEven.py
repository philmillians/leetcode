class Solution:
  def squareEven(self, arr1):
    j=0
    arr2=[]
    if arr1 == None:
      return None
    for i in range (len(arr1)):
      if i % 2 == 0:
        arr1[i]=arr1[i] ** 2
      else:
        arr1[i]
    return arr1

