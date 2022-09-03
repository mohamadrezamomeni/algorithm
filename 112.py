class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sum_all=0):
            if node:
                sum_all += node.val
                if sum_all == targetSum:
                    if node.left == None and node.right == None:
                        return True
                result_left = dfs(node.left, sum_all)
                if result_left == True:
                    return True
                result_right = dfs(node.right, sum_all)
                if result_right == True:
                    return True
                sum_all -= node.val
                return False
            return False

        return dfs(root)
