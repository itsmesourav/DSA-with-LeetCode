class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total = node.val + left_sum + right_sum
            count = 1 + left_count + right_count

            if total // count == node.val:
                ans += 1

            return total, count

        dfs(root)
        return ans