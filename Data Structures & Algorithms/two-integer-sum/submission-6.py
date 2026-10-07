class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums, start=0):
            value_needed = target - num
            if value_needed in nums:
                for j, numb in enumerate(nums, start=0):
                    if value_needed == numb and i!=j:
                        return [i,j]

