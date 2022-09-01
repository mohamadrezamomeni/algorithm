class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sort(left, right):
            if left == right:
                return None
            mid = (left+right)//2
            left = sort(left, mid)
            right = sort(mid+1, right)
            return TreeNode(nums[mid], left, right)
        return sort(0, len(nums))
