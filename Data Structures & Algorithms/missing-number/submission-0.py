class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x, y = nums[0], nums[-1]
        sum_nums = sum(nums)
        needed_sum = (y - x + 1) * (x + y) // 2
        return needed_sum - sum_nums