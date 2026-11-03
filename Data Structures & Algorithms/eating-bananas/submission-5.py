class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        minSpeed = right

        while left <= right:
            mid = (left + right) // 2

            banana_time = 0
            for p in piles:
                banana_time += math.ceil(p / mid)

            if banana_time <= h:
                minSpeed = min(minSpeed, mid)
                right = mid - 1
            else:
                left = mid + 1

        return minSpeed
                









        