class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = 0
        res_str = ""

        def is_palindrome(s):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(len(s)):
            for j in range(i, len(s)):
                curr = s[i:j+1]
                if is_palindrome(curr):
                    if len(curr) > res:
                        res_str = curr
                        res = len(curr)

        return res_str

