class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list_node = []
        node = head
        while True:
            if node is None:
                return False
            if node in list_node:
                return True
            list_node.append(node)
            node = node.next
