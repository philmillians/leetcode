#class Solution:
#    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#        hmap = {}
#        missingInts=[]
#        for i in nums:
#            hmap[i] = 1
#        for i in range(1,len(nums)+1):
#           if i not in hmap:
#                missingInts.append(i)
#        return missingInts
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missingInts=[]
        for i in range (len(nums)): 
            new_index = abs(nums[i]) - 1
            [nums[i]-1]*-1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        for j in range(1,len(nums)+1):
            if nums[j-1] > 0:
                missingInts.append(j)
        return missingInts
