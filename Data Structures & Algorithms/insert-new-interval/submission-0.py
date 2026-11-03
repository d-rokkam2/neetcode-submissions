class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key = lambda item:item[0])
        res = []

        for interval in intervals:

            if not res or res[-1][1] < interval[0]:
                res.append(interval)

            res[-1] = [res[-1][0], max(res[-1][1], interval[1])]

        return res