class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # cache = {0:0}

        # def dfs(i):
        #     if i in cache:
        #         return cache[i]

        #     count = float('inf')
        #     for coin in coins:
        #         if i - coin >= 0:
        #             count = min(count, 1 + dfs(i - coin))
            
        #     cache[i] = count
        #     return cache[i]

        # res = dfs(amount)
        # return res if res != float('inf') else -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for x in range(1, amount + 1):
            for c in coins:
                if x - c >= 0:
                    dp[x] = min(dp[x],1 + dp[x -c])

        return dp[-1] if dp[-1] != float('inf') else -1



        