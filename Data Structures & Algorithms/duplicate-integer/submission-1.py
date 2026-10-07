class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            new_num = [x for j, x in enumerate(nums) if j != i]
            if num in new_num:
                return True
        return False
        
        