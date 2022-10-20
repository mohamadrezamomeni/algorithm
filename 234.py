class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        return nums == nums[::-1]
