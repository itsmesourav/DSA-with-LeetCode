# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)    # Root
            dfs(node.left)          # Left
            dfs(node.right)         # Right

        dfs(root)
        return res