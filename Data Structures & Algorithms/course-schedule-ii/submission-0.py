from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = defaultdict(list)
        res = []
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        cycle = set()
        seen = set()
        def dfs(course):

            if course in cycle:
                return False

            if course in seen:
                return True

            cycle.add(course)
            for pre in adj_list[course]:
                if not dfs(pre):
                    return False

            seen.add(course)
            cycle.remove(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res 

