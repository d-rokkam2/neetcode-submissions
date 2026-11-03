from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n -1:
            return False

        adj = {i: [] for i in range(n)}
        for src, dst in edges:
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
            adj[src].append(dst)
            adj[dst].append(src)

        visit = set()
        dq = deque([0])
        visit.add(0)

        while dq:
            node = dq.popleft()
            for nei in adj[node]:
                if nei in visit:
                    continue
                visit.add(nei)
                dq.append(nei)
                
        return len(visit) == n



        
        