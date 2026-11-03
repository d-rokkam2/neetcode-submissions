class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = float('inf')
        maxProfit = 0

        for p in prices:
            minPrice = min(minPrice, p)
            maxProfit = max(p - minPrice, maxProfit)

        return maxProfit



        