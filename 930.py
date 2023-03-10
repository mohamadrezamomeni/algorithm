class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        presum = ans = 0
        store = {}
        for n in nums:
            if presum in store:
                store[presum] += 1  # count all presum and store it
            else:
                store[presum] = 1
            presum += n
            if presum-goal in store:  # check if subarray is available in the store
                ans += store[presum-goal]

        return ans
