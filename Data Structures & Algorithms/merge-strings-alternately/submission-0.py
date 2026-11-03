class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        minLength = min(len(word1), len(word2))
        res = ""
        for i in range(minLength):
            res += word1[i]
            res += word2[i]

        res += "".join(word1[minLength:])
        res += "".join(word2[minLength:])

        return res
        