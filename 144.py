class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return result
