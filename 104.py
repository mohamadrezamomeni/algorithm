class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, number=0):
            if node is None:
                return number
            number += 1
            if node.left is not None:
                left = dfs(node.left, number)
            else:
                left = number
            if node.right is not None:
                right = dfs(node.right, number)
            else:
                right = number
            if right > left:
                return right
            else:
                return left
        return dfs(root)
