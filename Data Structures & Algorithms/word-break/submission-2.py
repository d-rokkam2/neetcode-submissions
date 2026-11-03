class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        cache = {n : True}

        def dfs(i):

            if i in cache:
                return cache[i]

            cache[i] = False

            for w in wordDict:
                word_length = len(w)
                if i + word_length > n:
                    continue
                
                if s[i:i+word_length] == w:
                    if dfs(i + word_length):
                        cache[i] = True
                        break
            
            return cache[i]

        return dfs(0)

            


            

            

        