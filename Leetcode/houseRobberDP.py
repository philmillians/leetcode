class Solution:
    def rob(self, nums):
        # Special handling for empty case.
        if not nums:
          return 0
        maxRobbedAmount = [None for item in range(len(nums) + 1)]
        N = len(nums)
        # Base case initialization.
        maxRobbedAmount[N] = 0 
        maxRobbedAmount[N - 1] = nums[N - 1]
        # DP table calculations.
        for i in range(N - 2, -1, -1):   
            # Same as recursive solution.
          maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])    
        return maxRobbedAmount[0]    
        
nums=[2,7,9,3,1]
mySolution = Solution()
print(mySolution.rob(nums))
