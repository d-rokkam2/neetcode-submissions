class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        n = len(s)
        memo = {n : True}

        def dfs(i):
            if i in memo:
                return memo[i]

            memo[i] = False
            for w in wordDict:
                length = len(w)
                if i + length > n:
                    continue
                if s[i : i + length] == w:
                    if dfs(i + length):
                        memo[i] = True
                        break
                        
            return memo[i]
        return dfs(0)
            


            

            

        