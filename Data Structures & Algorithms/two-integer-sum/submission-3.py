class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums, 0):
            value_needed = target - num
            if value_needed in nums:
                j = nums.index(value_needed)
                if i != j:
                    return[i, j]

