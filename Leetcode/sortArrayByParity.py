class Solution:
  def sortArrayByParity(self, nums):
    j=0
    for i in range (len(nums)):
      if nums[i] % 2 == 0:
        temp = nums[j]
        nums[j]=nums[i]
        nums[i] = temp
        j+=1
    return nums 
