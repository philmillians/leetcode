class Solution:
    def rob(self, nums):
        # Special handling for empty case.
        if not nums:
            return 0
        N = len(nums)
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])
            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current
        return rob_next
      
nums=[2,7,9,3,1]
mySolution = Solution()
print(mySolution.rob(nums))
