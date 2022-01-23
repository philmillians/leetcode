class Node:
  def __init__(self,key,value=None):
    self.size = 0
    self.value=value
    self.key = key
class HashTable:
  INITIAL_CAPACITY=16

  def __init__(self):
    self.size=0
    self.capacity=16
    self.buckets= [None]*self.capacity
  def __str__(self):
    return str(self.__dict__)
  def insert(self,key,value):
    self.size +=1
    NewNode = Node(key,value)
    index = self.hash(key)
    node = self.buckets[index]
    if node ==None:
      self.buckets[index]=NewNode
      return
    previous = node
    while node:
      previous = node
      node = node.next
    previous.next = NewNode

  def remove(self,key):
    previous = None
    index = self.hash(key)
    node=self.buckets[index]
    while node and node.key != key:
      previous = node
      node = node.next
    if node == None:
      return None
    else:
      self.size -=1
      result = node.value
      if previous == None:
        node=None
      else:
        previous.next = previous.next.next
      return
  def hash(self,key):
    hashsum = 0
    for index, c in enumerate(key):
      hashsum += (index + len(key)) ** ord(c)
      hashsum = hashsum % self.capacity
    return hashsum

  def search(self,value):
    index = self.hash(key)
    node=self.buckets[index]
    while(node != None and node.key != key):
      node=node.next
    if node == None:
      print('key not in hashtable')
      return None
    return node.value
  def access(self,index):
    return self.buckets[index]
  def myLen(self):
    return self.size
