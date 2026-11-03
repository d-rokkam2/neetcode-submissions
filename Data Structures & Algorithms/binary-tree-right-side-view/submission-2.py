# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []

        def bfs(node):
            dq = deque()
            dq.append(node)
            while dq:
                level_size = len(dq)
                for i in range(level_size):
                    curr = dq.popleft()
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)

                    # checking if most right
                    if i == level_size - 1:
                        res.append(curr.val)
        bfs(root)    
        return res





        