class Solution:
    def rob(self, nums):
      def find(nums, index):
        maxOfIndexes=0
        for i in range(index,len(nums),2):
          maxOfIndexes += nums[i]
        return maxOfIndexes
      maxEvenIndexes = find(nums,0)
      maxOddIndexes = find(nums,1)
      if maxEvenIndexes > maxOddIndexes:
        return maxEvenIndexes
      elif maxEvenIndexes < maxOddIndexes:
        return maxOddIndexes
        
nums=[2,7,9,3,1]
mySolution = Solution()
print(mySolution.rob(nums))
