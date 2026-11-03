# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = defaultdict(list)

        def bfs(node):
            dq = deque()
            dq.append(node)
            level = 0
            while dq:
                for _ in range(len(dq)):
                    curr = dq.popleft()
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)
                    res[level].append(curr.val)
                level += 1

        if not root:
            return []

        bfs(root)
        return list(res.values())

                    


        

        







            
        