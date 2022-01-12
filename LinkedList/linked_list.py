class Node:
  def __init__(self,value=None):
    self.value=value
    self.next= None

class LinkedList:
  def __init__(self):
    self.head=None

  def addToEnd(self, newValue):
    NewNode = Node(newValue)
    if self.head == None:
      self.head = NewNode
      return
    lastNode = self.head
    while(lastNode.next):
      lastNode=lastNode.next
    lastNode.next= NewNode

  def addToBeginning(self, newValue):
    NewNode = Node(newValue)
    NewNode.next=self.head
    self.head = NewNode

  def remove(self, value):
    previousNode = None
    currentNode = self.head
    while currentNode:
      if currentNode.value == value:
        if previousNode:
          previousNode.next = currentNode.next
        else:
          self.head = currentNode.next
          return True
      previousNode = currentNode
      currentNode = currentNode.next
    return False

  def listPrint(self):
    if self.head == None:
      print("Nothing in LinkedList")
      return
    printValue = self.head
    while(printValue is not None):
      print(printValue.value)
      printValue=printValue.next

  def reverse(self):
    previousNode = None
    currentNode = self.head
    next = currentNode.next
    while(currentNode):
      next = currentNode.next
      currentNode.next = previousNode
      previousNode = currentNode
      currentNode = next
    self.head = previousNode

  def find(self, value):
    currentNode = self.head
    while (currentNode != None):
      if currentNode.value == value:
        print("We found that value")
        return True 
      currentNode = currentNode.next
    print("We didnt find that value")
    return False
