class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bfs(node, reverse: bool):
            result = []
            queue = [node]
            while len(queue) > 0:
                node = queue.pop(0)
                if node:
                    if reverse == True:
                        queue.append(node.left)
                        queue.append(node.right)
                    else:
                        queue.append(node.right)
                        queue.append(node.left)
                    result.append(node.val)
                else:
                    result.append(None)
            return result
        return bfs(root.left, False) == bfs(root.right, True)
