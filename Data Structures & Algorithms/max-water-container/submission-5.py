class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        l, r = 0, n - 1
        res = 0

        while l < r:
            minHeight = min(heights[l], heights[r])
            currArea = minHeight * (r - l)
            res = max(res, currArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res


        
        