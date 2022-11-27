class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_sum = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum < 1:
                max_sum = max(abs(prefix_sum), max_sum)
        return max_sum + 1
