class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = None
        n = len(nums)
        for i, num in enumerate(nums):
            if 0 > i and num == nums[i+1]:
                continue

            j = i+1
            k = n - 1
            while j < k:
                if result == None:
                    result = num + nums[j] + nums[k]
                else:
                    if abs(target - (num + nums[j] + nums[k])) < abs(target - result):
                        result = num + nums[j] + nums[k]
                    if target == num + nums[j] + nums[k]:
                        return target
                    if target < num + nums[j] + nums[k]:
                        k -= 1
                    else:
                        j += 1
        return result
