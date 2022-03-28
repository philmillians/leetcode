class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leftPtr=1
        for rightPtr in range(1,len(nums)):
            if nums[rightPtr] != nums[rightPtr-1]:
                nums[leftPtr] = nums[rightPtr]
                leftPtr += 1
        return leftPtr
