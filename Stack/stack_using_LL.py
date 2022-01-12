class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def pop(self):
    if self.top == None:
      return None
    currentNode = self.top  
    self.top = self.top.next
    self.length -= 1
    if self.length == 0:
      self.bottom = None
    return currentNode.value

  def push(self, newValue):
    NewNode = Node(newValue)
    if self.bottom == None:
      self.bottom = NewNode
      self.top = self.bottom
    else:
      self.top = NewNode
    self.length += 1

  def peek(self):
    return self.top.value

  def print(self):
    if self.top == None:
      print("Nothing in the queue")
      return
    printValue = self.top
    while printValue:
      print(self.top.value, end = ' -> ')
      printValue = printValue.next
      print()
