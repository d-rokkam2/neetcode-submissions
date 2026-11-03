class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)

        if len(s) != len(t):
            return False
            
        for c, c2 in zip(s,t):
            counter[c] += 1
            counter[c2] -= 1

        for val in counter.values():
            if val != 0:
                return False

        return True
        