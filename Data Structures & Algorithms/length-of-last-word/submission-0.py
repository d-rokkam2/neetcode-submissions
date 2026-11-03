class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        vals = s.split()
        return len(vals[-1])
        