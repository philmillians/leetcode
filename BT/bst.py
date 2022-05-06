class Node:
  def __init__(self, value):
    self.left=None
    self.right=None
    self.value = value
  def insert(self, value):
    NewNode = Node(value)
    if self.value == None:
      return False
    elif self.value > value:
      if self.left:
        return self.left.insert(value)
      else:
        self.left = NewNode
        return True
    else:
      if self.right:
        return self.right.insert(value)
      else:
        self.right = NewNode
        return True
  def find(self,value):
    if self.value == value:
      return True
    elif self.value > value and self.left:
      return self.left.find(value)
    elif self.value < value and self.right:
      return self.right.find(value)
    return False

  def preorder(self,list):
    list.append(self.data)
    if self.left:
      return self.left.preorder(list)
    if self.right:
      return self.right.preorder(list)
    return list

  def postorder(self,list):
    if self.left:
      return self.left.postorder(list)
    if self.right:
      return self.right.postorder(list)
    list.append(self.data)
    return list
  def inorder(self):
    if self.left:
      return self.left.inorder(list)
    list.append(self.data)
    if self.right:
      return self.right.inorder(list)
    return list
  def bfs(self, root=None):
    if root is None:
      return
    queue = [root]
    while len(queue) > 0:
      cur_node = queue.pop(0)
      if cur_node.left is not None:
        queue.append(cur_node.left)
      if cur_node.right is not None:
        queue.append(cur_node.right)
    return queue

class BST:
  def __init__(self,value):
    self.root = None
  def insert(self,newValue):
    NewNode = Node(newValue)
    if self.root:
      return self.root.insert(newValue)
    else:
      self.root = NewNode
      return True
  def find(self,value):
    if self.root:
      return self.root.find(value)
    else:
      return False
  def remove(self,value):
    pass  
  def preorder(self):
    if self.root:
      return self.root.preorder([])
    else:
      return []
  def postorder(self):
    if self.root:
      return self.root.postorder([])
    else:
      return []
  def inorder(self):
    if self.root:
      return self.root.inorder([])
    else:
      return []


