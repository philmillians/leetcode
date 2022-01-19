class Node:
  def __init__(self,value):
    self.data=value
    self.left=None
    self.right =None

  def insert(self,newValue):
    NewNode = Node(newValue)
    if self.data == newValue:
      return False
    elif self.data > newValue
      if self.left:
        return self.left.insert(newValue)
      else:
        self.left = NewNode
        return True
    else:
      if self.right:
        return self.right.insert(newValue)
      else:
        self.right = NewNode
        return True
  def find(self,value):
    if self.data == value:
      return True
    elif value < self.data and self.left:
      return self.left.find(value)
    elif value > self.data and self.right:
      return self.right.find(value)
	return False
  def inOrder(self):
    pass
  def postOrder(self):
    pass
  def preOrder(self):
    pass


class BST:
  def __init__(self,value):
    self.root = None

  def insert(self,newValue):
    pass
  def find(self,value):
    pass
  def remove(self,value):
    pass
  

