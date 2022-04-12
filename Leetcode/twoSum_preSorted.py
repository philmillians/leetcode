class Solution:
  def twoSum(self, nums, sum):
    low = 0;
    high = len(nums)-1
    tempSum=0
    while(low<high):
      tempSum=nums[low] + nums[high]
      if tempSum < sum:
        low +=1
      elif tempSum > sum:
        high -=1
      elif tempSum ==sum:
        return(nums[low],nums[high]) 
    return None
