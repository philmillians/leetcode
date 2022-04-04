class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #squaredNums = [n ** 2 for n in nums]
        #squaredNums.sort()
        #return squaredNums
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
