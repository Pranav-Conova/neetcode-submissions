class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        sum_nums = sum(nums)
        needed_sum = x * (x + 1) // 2
        return needed_sum - sum_nums