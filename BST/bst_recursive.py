def binary_search(array,low,high,index):
  if high >= low:
    mid = (high + low)
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      return binary_search(arr, low, mid - 1, x)
    else:
      return binary_search(arr, low, mid + 1, x)
  else:
    return -1
