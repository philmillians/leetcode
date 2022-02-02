class Solution:
  def maximumWealth(self, accounts):
    maxWealth = 0
    for item in accounts:
      currentCustomerWealth = sum(item)
      maxWealth = max(maxWealth, currentCustomerWealth)
    return maxWealth

accounts=[[2,8,7],[7,1,3],[1,9,5]]
mySolution = Solution()
print(mySolution.maximumWealth(accounts))
