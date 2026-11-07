class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        main_dict = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                main_dict.setdefault(s, []).append([i, j])

        final_set = set()

        for k, num in enumerate(nums):
            if -num in main_dict:
                for i, j in main_dict[-num]:
                    if k != i and k != j:
                        triplet = tuple(sorted([nums[i], nums[j], num]))
                        final_set.add(triplet)

        return [list(t) for t in final_set]


