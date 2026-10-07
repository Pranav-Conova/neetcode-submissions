import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)
        
        while stones:
            if len(stones) == 1:
                return -stones[0]
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                pass
            elif -x > -y:
                new_val = (-y) - (-x)
                heapq.heappush(stones, new_val)
            else:
                heapq.heappush(stones, x)
                heapq.heappush(stones, y)
        return 0

