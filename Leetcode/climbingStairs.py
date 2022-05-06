class Solution:
    def climbStairs(self, n: int) -> int:
        stairMap={}
        def dp(i):
            #Base cases
            if i <=2:
                return i
            #not a base case
            if i not in stairMap:
                stairMap[i] = dp(i-1) + dp(i-2)
            return stairMap[i]
        return dp(n)
