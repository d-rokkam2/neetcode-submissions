class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {0:0}

        def dfs(i):
            if i in cache:
                return cache[i]

            count = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    count = min(count, 1 + dfs(i - coin))
            
            cache[i] = count
            return cache[i]

        res = dfs(amount)
        return res if res != float('inf') else -1



        