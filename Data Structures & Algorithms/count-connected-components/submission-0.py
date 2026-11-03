from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_list = {i:[] for i in range(n)}

        for src, dst in edges:
            if src not in adj_list:
                adj_list[src] = []
            if dst not in adj_list:
                adj_list[dst] = []

            adj_list[src].append(dst)
            adj_list[dst].append(src)

        visit = set()

        def bfs(node):
            dq = deque([node])

            while dq:
                node = dq.popleft()
                for nei in adj_list[node]:
                    if nei not in visit:
                        visit.add(nei)
                        dq.append(nei)
        res = 0
        for node in range(n):
            if node not in visit:
                bfs(node)
                res += 1

        return res



        
        