class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        n = len(arrays)
        currMin, currMax = arrays[0][0], arrays[0][-1]
        res = 0

        for arr in arrays:
            res = max(arr[-1] - currMin, currMax - arr[0])
            currMax = max(currMax, arr[-1])
            currMin = max(currMin, arr[0])

        return res



        