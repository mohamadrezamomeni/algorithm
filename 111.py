class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mD=0):
            lM = None
            rM = None
            if node:
                mD += 1
                if node.left is not None:
                    lM = dfs(node.left, mD)
                if node.right is not None:
                    rM = dfs(node.right, mD)
            if lM is not None and rM is not None:
                return min(lM, rM)
            elif lM:
                return lM
            elif rM:
                return rM
            else:
                return mD
        return dfs(root)
