import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append((math.prod(nums[(i+1):]) or 0) * (math.prod(nums[:i]) or 0))
        return result