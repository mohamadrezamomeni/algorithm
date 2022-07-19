class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = tail = ListNode(-1)
        if len(lists) == 0:
            return None
        for i, link in enumerate(lists):
            if link:
                heapq.heappush(heap, (link.val, i))
        if len(heap) == 0:
            return None
        while heap:
            val, i = heapq.heappop(heap)
            tail.next = ListNode(val)
            tail = tail.next

            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        return head.next
