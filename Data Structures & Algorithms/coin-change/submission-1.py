class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {0 :0}
        def dfs(amt):
            if amt in cache:
                return cache[amt]

            count = float('inf')
            for n in coins:
                if amt - n >= 0:
                    count = min(count, 1 + dfs(amt - n))

            cache[amt] = count
            return cache[amt]
        
        minCoins = dfs(amount)

        return minCoins if minCoins != float('inf') else -1





        
        