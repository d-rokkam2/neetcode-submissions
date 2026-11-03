class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r

        while l <= r:

            banana_time = 0
            rate = (l + r) // 2

            for p in piles:
                banana_time += math.ceil(p / rate)

            if banana_time <= h:
                res = min(res, rate)
                r = rate - 1
            else:
                l = rate + 1
            
        return res

