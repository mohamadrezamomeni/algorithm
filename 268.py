class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums)
        memory = {}
        for num in nums:
            memory[num] = True

        for i in range(len_nums+1):
            if i not in memory:
                return i
