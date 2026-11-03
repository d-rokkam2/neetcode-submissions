class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxChars = 0
        ret = 0
        l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxChars = max(maxChars, count[s[r]])
            while (r - l + 1) - maxChars > k:
                count[s[l]] -= 1
                l += 1

            ret = max(ret, r - l + 1)

        return ret
