class Solution:
    def trap(self, height: List[int]) -> int:

        totWater = 0
        n = len(height)

        for i in range(n):

            maxLeft = maxRight = float('-inf')

            for j in range(i):
                maxLeft = max(maxLeft, height[j])

            for k in range(i + 1, n):
                maxRight = max(maxRight, height[k])

            currWater = min(maxRight, maxLeft) - height[i]

            if currWater < 0:
                continue

            totWater += currWater

        return totWater

        