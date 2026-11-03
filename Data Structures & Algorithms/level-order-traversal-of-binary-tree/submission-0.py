from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = defaultdict(list)

        if not root:
            return []

        def bfs(node):
            
            dq = deque()
            level = 0

            if not node:
                return None
        
            dq.append(node)

            while dq:
                for i in range(len(dq)):
                    curr = dq.popleft()
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)
                    res[level].append(curr.val)
                level += 1

        bfs(root)
        return list(res.values())





            

            



        