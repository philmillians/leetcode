INITIAL_CAPACITY=16
class ArrayList:
  def __init__(self,size):
    self.size = 0
    self.capacity=INITIAL_CAPACITY
    self.data = {}
  def __str__(self):
    return str(self.__dict__)
  def access(self,index):
    if index > self.size:
      print("index out of range")
      return
    return self.data[index]
  def insertAtIndex(self,index, newValue):
    self.data[index]=newValue
    self.size +=1
    return
  def insertAtEnd(self,newValue):
    self.data[self.size]=newValue
    self.size +=1
    return
  def insert(self,newValue,index):
    self.data[index]=newValue
    self.size += 1
    return
  # def insertAtBeginning(self,newValue):
  #   for item in self.data:
  #     index += 
  #   return self.data[0]=newValue
  #   self.size +=1
  def search(self,value):
    for item in range(self.size):
      if self.data[item]==value:
        print(f'Found {value} at index: {item}')
        return self.data[item]
  def delete(self,value):
    del self.data[value] 
    self.size -=1
  
  def myLen(self):
    print(self.size)
    return self.size
