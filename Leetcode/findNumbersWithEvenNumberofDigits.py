class Solution:
    def findNumbers(self, nums: List[int]) -> int:
      str_nums = map(str,nums)
      counter = 0
      for n in str_nums:
        if len(n) % 2 == 0:
          counter += 1
      return counter
