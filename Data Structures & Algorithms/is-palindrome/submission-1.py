class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        f_s = "".join([s.lower() for s in s if s.isalnum()])

        return f_s == f_s[::-1]
        