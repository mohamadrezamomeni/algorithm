class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        root_node = ListNode()
        node = None
        a_node = list1
        b_node = list2
        while True:
            if a_node == None and b_node == None:
                break
            if node == None:
                node = root_node
            else:
                node.next = ListNode()
                node = node.next

            if a_node == None:
                node.val = b_node.val
                b_node = b_node.next
                continue
            if b_node == None:
                node.val = a_node.val
                a_node = a_node.next
                continue
            if a_node.val <= b_node.val:
                node.val = a_node.val
                a_node = a_node.next
            else:
                node.val = b_node.val
                b_node = b_node.next
        return root_node
