class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, result):
            if node:
                dfs(node.left, result)
                dfs(node.right, result)
                result.append(node.val)
        dfs(root, ans)
        return ans
