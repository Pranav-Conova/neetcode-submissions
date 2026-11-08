class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      a = nums[0]
      for num in nums[1:]:
        a = a ^ num
      return a