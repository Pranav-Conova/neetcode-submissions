import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        heap = [(-value, key) for key, value in hash_map.items()]
        heapq.heapify(heap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
        