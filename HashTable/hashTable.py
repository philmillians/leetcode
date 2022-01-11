INITIAL_CAPACITY = 16   
class Node:
  def __init__(self,key,value=None):
    self.key = key
    self.value = value
    self.next = None
  
  def __str__(self):
    return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
  
  def __repr__(self):
    return str(self)

class HashTable():
  def __init__(self):
    self.capacity = INITIAL_CAPACITY
    self.buckets = [None]*self.capacity
    self.size = 0
  
  def __str__(self):
    return str(self.__dict__)
  
  def hash(self, key):
    hashsum = 0
    for index, c in enumerate(key):
  # Add (index + length of key) ^ (current char code)
      hashsum += (index + len(key)) ** ord(c)
  # Perform modulus to keep hashsum in range [0, self.capacity - 1]
      hashsum = hashsum % self.capacity
    return hashsum
  
  def find(self, value):
    index = self.hash(key)
    node = self.buckets[index]
    while (node != None and node.key != key):
      node = node.next
    if node == None:
      print("Key not in HashTable")
      return None
    return node.value
  
  def add(self, key, value):
    self.size += 1
    NewNode = Node(key,value)
    index = self.hash(key)
    node = self.buckets[index]
    if node is None:
      self.buckets[index] = NewNode
      return
    previous = node
    while node is not None:
      previous = node
      node = node.next
    previous.next = NewNode

  def remove(self, key):
    self.size -= 1
  
  def remove(self, key):
    index = self.hash(key)
    node = self.buckets[index]
    previous = None
    while node is not None and node.key != key:
      previous = node
      node = node.next
    if node is None:
      return None
    else:
      self.size -= 1
      result = node.value
      if previous is None:
        self.buckets[index] = node.next 
      else:
        previous.next = prev.next.next 
        return result 
