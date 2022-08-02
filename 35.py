class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            print(mid)
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return start
