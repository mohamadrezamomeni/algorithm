class Solution(object):
    def twoSum(self, nums, target):
        results = []
        for i1, v1 in enumerate(nums):
            for j1, v2 in enumerate(nums):
                if v2 + v1 == target and i1 != j1:
                    results.append(i1)
                    results.append(j1)
                    return results
