from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        count = defaultdict(list)
        for course, prereq in prerequisites:
            count[course].append(prereq)

        seen = set()

        def dfs(course):

            if course in seen:
                return False

            if count[course] == []:
                return True

            seen.add(course)
            for pre in count[course]:
                if not dfs(pre):
                    return False
            
            seen.remove(course)
            count[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


        
