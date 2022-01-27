class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    map = {}
    for item in range(len(nums)):
      complement = target - nums[item]
      if(complement in map):
        return (map[complement],item)
      map[nums[item]]=item
    return None
