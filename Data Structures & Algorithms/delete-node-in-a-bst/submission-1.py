# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def getMin(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, val)
        elif key < root.val:
            root.left = self.deleteNode(root.left, val)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            else:
                placeholder = getMin(root.right)
                root.val = placeholder.val
                root.right = self.deleteNode(root.right, placeholder.val)

        return root



        