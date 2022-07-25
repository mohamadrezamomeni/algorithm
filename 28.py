class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        length = len(nums)
        i = 1
        while True:
            if i >= length:
                break
            if nums[i-1] == nums[i]:
                i += 1
            else:
                count += 1
                nums[count] = nums[i]
                i += 1
        return count + 1
