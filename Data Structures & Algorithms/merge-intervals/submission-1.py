class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda item:item[0])
        res = []

        for i in intervals:

            if not res or res[-1][1] < i[0]:
                res.append(i)

            res[-1] = [res[-1][0], max(i[1], res[-1][1])]

        return res

        