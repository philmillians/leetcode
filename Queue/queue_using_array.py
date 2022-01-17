class Queue:
  def __init__(self,value=0):
    self.size = value
    self.data = list()
  def __str__(self):
    return str(self.data)
  def enqueue(self,newValue):
    self.data.append(newValue)
    self.size +=1
    return
  def dequeue(self):
    print(self.data.pop())
    self.size -=1
    return
  def find(self,value):
    for item in range(self.size):
      if self.data[item]==value:
        print(f'Found {value} at index: {item}')
        return  
    print('Item not in queue')
    return
  def myLen(self):
    print(self.size)
    return self.size
  def peek(self):
    return self.data[self.size-1]
