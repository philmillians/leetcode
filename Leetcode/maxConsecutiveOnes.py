class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        output = 0
        for r,n in enumerate(nums):
          if n == 0:
            l = r+1
          output= max(output,r-l+1)
        return output
