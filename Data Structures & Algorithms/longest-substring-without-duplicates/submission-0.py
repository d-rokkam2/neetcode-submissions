class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxSub = 0
        l = 0
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            maxSub = max(maxSub, len(char_set))

        return maxSub

            


        





        