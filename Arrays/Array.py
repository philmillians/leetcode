class ArrayList:
  def __init__(self,value=None):
    self.size = value
    self.data = {}

  def __str__(self):
    return str(self.__dict__)

  def access(self,index):
    if index > self.size:
      print("index out of range")
      return
    print(self.data[index])
    return self.data[index]
  def search(self,value):
    for item in self.data:
      if self.data[item] == value:
        print(f'Found {value} at index: {item}')
        return
  def delete(self,value):
    deletedItem = self.search(value)
    previous
    
  def insert(self,newValue,index):
    self.data[index]=newValue
    self.size += 1
    return
  def myLen(self):
    print(self.size)
    return self.size
