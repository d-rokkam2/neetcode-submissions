class Solution:
    def romanToInt(self, s: str) -> int:

        conversions = {
            'I':             1,
            'V':             5,
            'X':            10,
            'L':             50,
            'C':             100,
            'D':             500,
            'M':             1000
        }

        ret = 0
        n = len(s)

        for i in range(n):
            curr = conversions[s[i]]
            if i != n - 1 and curr < conversions[s[i + 1]]:
                ret -= curr
            else:
                ret += curr

        return ret
                




        