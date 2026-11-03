class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = res = 0
        n = len(s)
        character_set = set()

        for right in range(n):

            while s[right] in character_set:
                character_set.remove(s[left])
                left += 1

            character_set.add(s[right])
            res = max(len(character_set), res)

        return res


        