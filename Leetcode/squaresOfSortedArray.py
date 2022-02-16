class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredNums = [n ** 2 for n in nums]
        squaredNums.sort()
        return squaredNums
