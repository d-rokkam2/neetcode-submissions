class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = maxLen = 0
        n = len(s)
        charSet = set()

        for right in range(n):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            maxLen = max(maxLen, len(charSet))

        return maxLen

        