class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = float('inf')
        maxProf = 0

        for p in prices:
            
            minPrice = min(minPrice, p)
            maxProf = max(p - minPrice, maxProf)

        return maxProf

        



        