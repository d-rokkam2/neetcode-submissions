class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        right = len(needle)
        left = 0

        while right <= n:
            if haystack[left:right] == needle:
                return left
            else:
                left += 1
                right += 1
                continue

        return -1




        