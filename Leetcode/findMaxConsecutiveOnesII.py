class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        leftPtr=0
        rightPtr=0
        maxOnes=0
        numberOfZeros=0
        while rightPtr < len(nums):
            if nums[rightPtr]==0:
                numberOfZeros+=1
            while numberOfZeros==2:
                if nums[leftPtr]==0:
                    numberOfZeros -=1
                leftPtr +=1
            maxOnes=max(maxOnes, rightPtr-leftPtr + 1)
            rightPtr +=1
        return maxOnes
