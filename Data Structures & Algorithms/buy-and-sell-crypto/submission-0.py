class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = []
        for i, x in enumerate(prices):
            if prices[i+1:] and max(prices[i+1:]) > x:
                result.append(max(prices[i+1:])-x)
        return max(result) if result else 0