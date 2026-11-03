class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        adj = {i:[] for i in range(1, n + 1)}
        
        def dfs(node, par):
            if node in visit:
                return True
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True

            return False

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
            visit = set()
            if dfs(src, -1):
                return [src, dst]

        return []


        




        