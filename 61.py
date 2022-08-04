class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        length = 1

        last_node = head
        while last_node.next is not None:
            last_node = last_node.next
            length += 1

        k = k % length

        last_node.next = head
        node = last_node
        previous = None
        for _ in range(length - (k - 1)):
            previous = node
            node = node.next

        previous.next = None
        return node
