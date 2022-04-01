class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if (len(nums))<3:
            return max(nums)
        #Get Max1
        max1=max(nums)
        #Get max2
        nums2=[]
        for i in range(len(nums)):
            if nums[i]!=max1:
                nums2.append(nums[i])
                max2=max(nums2)
    #Get max3
        nums3=[]
        for i in range(len(nums)):
            if nums[i]!=max1 and nums[i]!=max2:
                nums3.append(nums[i])
                max3=max(nums3)
        return max3
