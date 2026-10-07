class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def kth_largest(self):
        return sorted(self.nums, reverse=True)[self.k - 1]

    def add(self, val: int) -> int:
        self.nums.append(val)
        return self.kth_largest()