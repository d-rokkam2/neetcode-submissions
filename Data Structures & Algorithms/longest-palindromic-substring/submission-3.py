class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resLen = 0
        def checker(l, r) -> None:
            nonlocal res, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l -= 1
                r += 1
                    
        for i in range(len(s)):
            l, r = i, i
            checker(l, r)
            checker(l, r + 1)

        return res

            
            

        