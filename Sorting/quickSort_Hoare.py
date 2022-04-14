def quickSort(array,start,end):
 if start<end:
    p=partition(array,start,end)
    quickSort(array,start,p-1)
    quickSort(array,p+1,end)

def partition(array,start,end):
  i=start
  j=end-1
  pivotValue=array[end]
  while i < j:
    while array[i] < pivotValue and i < end:
      i+=1
    while array[j] >= pivotValue and j > start:
      j-=1
    if i < j:
      array[i],array[j] = array[j], array[i]
  if array[i] > pivotValue:
    array[i],array[end] = array[end], array[i]
  return i
