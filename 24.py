class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursiveChange(node):
            if not node or not node.next:
                return node

            temp = node.next.next
            next_node = node.next
            node.next = recursiveChange(temp)
            next_node.next = node

            return next_node

        return recursiveChange(head)
