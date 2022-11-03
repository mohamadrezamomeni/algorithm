class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memory = {}
        for i in nums1:
            if i not in memory:
                memory[i] = 1
            else:
                memory[i] += 1

        result = []
        for i in nums2:
            if i in memory and memory[i] > 0:
                result.append(i)
                memory[i] -= 1
        return result
