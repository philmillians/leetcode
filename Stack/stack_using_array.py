class Stack:
  def __init__(self):
    self.arr = []
    self.length = 0
    self.capacity = 16

  def __str__(self):
    return str(self.arr)

  def peek(self):
    return self.arr[self.length-1]

  def push(self, value):
    self.arr.append(value)
    self.length += 1

  def pop(self):
    deletedItem = self.arr[self.length-1]
    del self.arr[self.length-1]
    self.length -= 1
    return deletedItem
  def myLen(self):
    print(self.length)
    return self.length + 1

  def search(self,value):
    for item in range(self.length):
      if self.arr[item]==value:
        print(f'Found {value} at index: {item}')
        return
    print('Item not in stack')
    return
