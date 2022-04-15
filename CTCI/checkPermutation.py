class Solution:
  def checkPermutation(self,string1,string2):
    
    if (len(string1) > 128 or len(string2) > 128):
      print('check the input; greater than 128')
      return False
    if (len(string1) != len(string2)):
      print("No, not a Permutation,lengths not equal")
      return False
    sorted_string1=sorted(string1)
    sorted_string2=sorted(string2)
    if(sorted_string1 == sorted_string2):
      print("Yes, Permutation")
    else:
      print("No, not a Permutation")
