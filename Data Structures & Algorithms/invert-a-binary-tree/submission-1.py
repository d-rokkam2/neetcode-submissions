# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def bfs(node):

            if not node:
                return None

            dq = deque([node])

            while dq:
                curr = dq.popleft()
                curr.left, curr.right = curr.right, curr.left
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)

            return node

        return bfs(root)

            
            
        