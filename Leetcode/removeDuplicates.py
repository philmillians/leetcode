def removeDuplicates(self, nums) :
      i=0
      for item in range(1,len(nums)):
        if nums[item] != nums[i]:
          i+=1
          nums[i]=nums[item]
      print(nums)
      return i + 1
