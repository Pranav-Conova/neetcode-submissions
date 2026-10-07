class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f = 0
        r = len(nums) -1
        while f <= r:
            half_value = (f + r + 1) // 2
            if nums[half_value] == target:
                return half_value
            elif nums[half_value] > target:
                r = half_value - 1
            else:
                f = half_value + 1
        return -1