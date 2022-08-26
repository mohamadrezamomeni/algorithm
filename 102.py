class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node, depth=0):
            if node:
                if len(result) >= depth+1:
                    result[depth].append(node.val)
                else:
                    result.append([node.val])

                dfs(node.left, depth+1)
                dfs(node.right, depth+1)
        dfs(root)
        return result
