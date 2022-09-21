class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_link_list = [head]
        if head is None:
            return head
        node = head.next
        while True:
            if node is not None:
                list_link_list.append(node)
                node = node.next
            else:
                break

        def mergeSort(list_node):

            len_list_node = len(list_node)
            if len_list_node == 1:
                return list_node

            mid = len_list_node // 2

            left = mergeSort(list_node[:mid])
            right = mergeSort(list_node[mid:])
            left_len = len(left)
            right_len = len(right)
            result = []
            i = 0
            j = 0
            while i < right_len and j < left_len:
                if right[i].val > left[j].val:
                    result.append(left[j])
                    j += 1
                else:
                    result.append(right[i])
                    i += 1

            result += right[i:]
            result += left[j:]

            return result

        sorted_list = mergeSort(list_link_list)
        len_sorted_list = len(sorted_list)
        for i, node in enumerate(sorted_list):
            if i+1 != len_sorted_list:
                node.next = sorted_list[i+1]
            else:
                node.next = None
        return sorted_list[0]
