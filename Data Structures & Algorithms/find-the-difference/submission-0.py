class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(t)
        for char in s:
            count[char] -= 1

        for c in t:
            if count[c] == 1:
                return c

                


        