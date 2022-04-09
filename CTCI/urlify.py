class Solution:
  def urlify(self,string1,size):
    list1 = list(string1)
    for i in range (0,size-1):
      if list1[i]==" ":
        list1[i] = '%20'
    string1=(''.join(list1))
    return string1
