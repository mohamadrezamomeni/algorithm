class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while True:
            if node is None or node.next is None:
                return head
            next_node = node.next
            if next_node.val == node.val:
                node.next = next_node.next
            else:
                node = node.next
        return node
