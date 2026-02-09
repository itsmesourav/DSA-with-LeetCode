# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inOrder = []
        self.leetcode(root, inOrder)
        return self.balanced(inOrder)

    def leetcode(self, root, inOrder):
        if not root:
            return
        self.leetcode(root.left, inOrder)
        inOrder.append(root.val)
        self.leetcode(root.right, inOrder)

    def balanced(self, inOrder):
        if not inOrder:
            return
        mid = len(inOrder)//2
        root = TreeNode(inOrder[mid])
        root.left = self.balanced(inOrder[:mid])
        root.right = self.balanced(inOrder[mid+1:])
        return root