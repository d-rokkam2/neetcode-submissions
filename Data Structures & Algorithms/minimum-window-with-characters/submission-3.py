from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        tCount = Counter(t)
        sCount = Counter()
        l = 0
        have = 0
        resLen = float('inf')
        ret_r, ret_l = 0,0
        need = len(tCount)

        for r in range(len(s)):
            char = s[r]
            sCount[char] = sCount.get(char, 0) + 1
            if char in tCount and tCount[char] == sCount[char]:
                have += 1

            while have == need:

                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    ret_r, ret_l = r, l
                
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        return s[ret_l : ret_r + 1 ] if resLen != float('inf') else ""







            






        