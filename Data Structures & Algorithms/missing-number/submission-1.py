class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x, y = min(nums), max(nums)
        sum_nums = sum(nums)
        needed_sum = (y - x + 1) * (x + y) // 2
        return needed_sum - sum_nums