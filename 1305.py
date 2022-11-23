class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node, stack=[]):
            if node.left is not None:
                dfs(node.left, stack)

            stack.append(node.val)

            if node.right is not None:
                dfs(node.right, stack)

            return stack

        stacka = []
        stackb = []

        if root1 is not None:
            stack1 = dfs(root1, stacka)
        else:
            stack1 = []

        if root2 is not None:
            stack2 = dfs(root2, stackb)
        else:
            stack2 = []

        len_1 = len(stack1)
        len_2 = len(stack2)

        i = 0
        j = 0

        result = []
        while i < len_1 or j < len_2:
            if i >= len_1:
                result.append(stack2[j])
                j += 1
                continue

            if j >= len_2:
                result.append(stack1[i])
                i += 1
                continue

            if stack1[i] > stack2[j]:
                result.append(stack2[j])
                j += 1
            else:
                result.append(stack1[i])
                i += 1
        return result
