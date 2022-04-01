class Solution:
    def thirdMax(self, nums):
        # Remove duplicates in list by converting to set.
        nums = set(nums)
        # Find the max.
        maximum = max(nums)
        # Check is less than 3.
        if len(nums) < 3:
            return maximum
        # Remove 1st and 2nd max.
        nums.remove(maximum)
        second_maximum = max(nums)
        nums.remove(second_maximum)
        # Return 3rd max.
        return max(nums)
