class Node:
  def __init__(self,value=None):
    self.value = value
    self.previous = None
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def enqueue(self, newValue):
    NewNode = Node(newValue)
    # if self.head == None:
    #   self.head = NewNode
    #   self.tail = self.head
    # else:
    #   self.tail.next = NewNode
    #   self.next = NewNode
    # self.size += 1
    if self.size > 0:
      self.tail.previous = NewNode
      NewNode.next = self.tail
      self.tail = NewNode
    else:
      self.head = NewNode
      self.tail = NewNode
    self.size += 1

  def dequeue(self, value):
    lastNode=self.head
    while(lastNode):
      lastNode = lastNode.next

  def peek(self):
    if self.head:
      print(self.head.value)
      return self.head.value
    print("Nothing in Queue")
    return None

  def getSize(self):
    print(self.size)
    return self.size  

  def print(self):
    if self.head == None:
      print("Nothing in the queue")
      return
    printValue = self.head
    while (printValue is not None):
      print(printValue.value)
      printValue = printValue.next
