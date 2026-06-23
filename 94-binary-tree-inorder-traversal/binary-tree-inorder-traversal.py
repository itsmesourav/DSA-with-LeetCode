class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
        dfs (root)
        return result