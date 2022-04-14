def mergeSort(array):
  if len(array) < 2:
    return
  middle = len(array) // 2
  left = array[:middle]
  right= array[middle:]
  mergeSort(left)
  mergeSort(right)
  merge(array,left,right)
def merge(array,left,right):
  i=0
  j=0
  k=0
  while i < len(left) and j < len(right):
    if left[i] < right [j]:
      array[k] = left[i]
      i+=1
    else:
     array[k] = right[j]
     j+=1
    k+=1
  while i < len(left):
    array[k]=left[i]
    i+=1
    k+=1
  while j < len(right):
   array[k]=right[j]
   j+=1
   k+=1
