class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for item in range(0,len(nums)):
            if nums[item]!=val:
                nums[k]=nums[item]
                k+=1
        return k
