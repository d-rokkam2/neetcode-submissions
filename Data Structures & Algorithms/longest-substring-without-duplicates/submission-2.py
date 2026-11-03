class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        maxx = 0
        character_set = set()
        
        for right in range(len(s)):

            while s[right] in character_set:
                character_set.remove(s[left])
                left += 1

            character_set.add(s[right])
            maxx = max(len(character_set), maxx)

        return maxx
