class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        def bfs(root):
            queue = [root]

            result = []
            while True:
                if len(queue) == 0:
                    return result
                t = queue.pop()
                if t is not None:
                    result.append(t.val)
                else:
                    result.append(t)
                if t is None:
                    continue
                queue.append(t.right)
                queue.append(t.left)

        return bfs(p) == bfs(q)
