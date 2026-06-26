class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def mirror(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return (mirror(left.left, right.right) and
                    mirror(left.right, right.left))

        return mirror(root.left, root.right)