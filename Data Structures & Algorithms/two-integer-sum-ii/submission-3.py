class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(numbers)):
            hash_map[numbers[i]] = i+1
            needed = target - numbers[i]
            if needed in hash_map and numbers[i] != needed:
                return [hash_map[target - numbers[i]], i+1]