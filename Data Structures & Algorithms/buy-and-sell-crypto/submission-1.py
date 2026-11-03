class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minPrice = float('inf')

        for price in prices:
            
            if price < minPrice:
                minPrice = price

            currProfit = price - minPrice

            if currProfit > maxProfit:
                maxProfit = currProfit

        
        return maxProfit
