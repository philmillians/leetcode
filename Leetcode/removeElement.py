class Solution:
    def removeElement(self, nums, val):
        j = len(nums) - 1
        i =0
        while i < len(nums) and i < j:
            if nums[i] == val :
                if nums[j] == val :
                    j -=1
                else :
                    nums[i],nums[j] = nums[j],val
                    i +=1
                    j-=1
            else :
                i +=1
        count=0
        for i in range(len(nums)) :
            if val != nums[i] :
                count +=1
        return count
    
