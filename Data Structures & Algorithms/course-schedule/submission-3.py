class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        seen = set()
        def dfs(course):

            if course in seen:
                return False
            
            if adj[course] == []:
                return True

            seen.add(course)
            for cls in adj[course]:
                if not dfs(cls):
                    return False

            seen.remove(course)
            adj[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True



        