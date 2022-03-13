class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in range (len(nums)):
            if nums[i]==0:
                count += 1
            else:
                nums[i-count]=nums[i]
        for j in range (len(nums)-count,len(nums)):
            nums[j]=0
        return nums

# i = 0
      #   j = i+1
      #   count = 0
      #   while count<len(nums)-1 and len(nums)>1:
      #       if nums[i] != 0:
      #           i+=1
      #           j+=1
      #       elif nums[i] == 0 and nums[j] == 0:
      #           j+=1
      #       elif nums[i] == 0 and nums[j] != 0:
      #           nums[i],nums[j] = nums[j],nums[i]
      #           i+=1
      #           j+=1
      #       count+=1
