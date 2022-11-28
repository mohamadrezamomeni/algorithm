class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = 0
        for i, num in enumerate(nums):
            if i == 0:
                continue
            nums[i] = num + nums[i-1]
        return nums
