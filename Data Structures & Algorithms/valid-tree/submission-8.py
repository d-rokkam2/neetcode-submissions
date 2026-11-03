from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n -1:
            return False

        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        seen = set()
        dq = deque([(0,-1)])
        seen.add(0)

        while dq:
            node, parent = dq.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False

                seen.add(nei)
                dq.append((nei,node))

        return len(seen) == n





        
        