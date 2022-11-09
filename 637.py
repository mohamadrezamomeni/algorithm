from collections import deque


class Solution:
    def averageOfLevels(self, root):
        queue = []
        res = []
        queue.append(root)

        while queue:
            sum_level = 0
            lenq = len(queue)
            for i in range(lenq):
                node = queue.pop(0)
                sum_level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sum_level/lenq)
        return res
