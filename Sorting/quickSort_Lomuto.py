def quickSort(array,start,end):
  if start < end:
    p=partition(array,start,end)
    quickSort(array,start,p-1)
    quickSort(array,p+1,end)
def partition(array,start,end):
  pivotIndex=start
  pivotValue=array[end]
  i=start
  for i in range(start,end):
    if i >= end:
      return
    if pivotValue > array[i]:
      array[i],array[pivotIndex]=array[pivotIndex],array[i]
      pivotIndex+=1
  array[end],array[pivotIndex]=array[pivotIndex],array[end]
  return pivotIndex
