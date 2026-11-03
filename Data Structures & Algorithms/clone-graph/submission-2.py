"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        copy = {}
        copy[node] = Node(node.val)
        dq = deque([node])

        while dq:
            curr = dq.popleft()
            for nei in curr.neighbors:
                if nei not in copy:
                    copy[nei] = Node(nei.val)
                    dq.append(nei)
                copy[curr].neighbors.append(copy[nei])

        return copy[node]
                






        
        
        