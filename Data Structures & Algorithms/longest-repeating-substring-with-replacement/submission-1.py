class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxx = 0
        left = 0
        res = 0
        cnt = {}
        n = len(s)

        for right in range(n):  
            cnt[s[right]] = cnt.get(s[right], 0) + 1
            maxx = max(maxx, cnt[s[right]])
            
            while (right - left + 1) - maxx > k:
                cnt[s[left]] -= 1
                left += 1

            res = max(res, right-left + 1)

        return res



        







                



        