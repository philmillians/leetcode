class Stack:
  def __init__(self):
    self.arr = []
    self.length = 0

  def __str__(self):
    return str(self.__dict__)

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
