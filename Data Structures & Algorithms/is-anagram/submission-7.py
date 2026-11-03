from collections import defaultdict
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        freq = defaultdict(int)

        for char in s:
            freq[char] += 1

        for i in t:
            if i in freq and freq[i] > 0:
                freq[i] = freq[i] - 1
            else:
                return False

        return True


        
        