class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        candidate = 0

        for num in nums:
            if counter == 0:
                candidate = num
            counter += 1 if num == candidate else -1
        return candidate
