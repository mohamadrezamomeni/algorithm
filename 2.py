class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        resultHeadLinkList = resultLinkList = ListNode()
        carry = 0
        while node1 is not None and node2 is not None:
            val1 = node1.val
            val2 = node2.val
            result = val1 + val2 + carry
            if result >= 10:
                carry = 1
                result -= 10
            else:
                carry = 0
            resultLinkList.val = result

            if node1.next is not None or node2.next is not None:
                resultLinkList.next = ListNode()
                resultLinkList = resultLinkList.next
            node1 = node1.next
            node2 = node2.next

        while node1 is not None:
            val1 = node1.val
            result = val1 + carry
            if result >= 10:
                carry = 1
                result -= 10
            else:
                carry = 0

            resultLinkList.val = result
            if node1.next is not None:
                resultLinkList.next = ListNode()
                resultLinkList = resultLinkList.next
            node1 = node1.next

        while node2 is not None:
            val2 = node2.val
            result = val2 + carry
            if result >= 10:
                carry = 1
                result -= 10
            else:
                carry = 0

            resultLinkList.val = result
            if node2.next is not None:
                resultLinkList.next = ListNode()
                resultLinkList = resultLinkList.next
            node2 = node2.next

        if carry == 1:
            resultLinkList.next = ListNode(1)

        return resultHeadLinkList
