class Solution(object):
    def averageOfSubtree(self, root):
        ans = [0]

        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total = node.val + left_sum + right_sum
            count = 1 + left_count + right_count

            if total // count == node.val:
                ans[0] += 1

            return total, count

        dfs(root)
        return ans[0]