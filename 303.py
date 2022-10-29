class NumArray:

    prefix_sum = []

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        pre_sum = 0
        for num in nums:
            pre_sum += num
            self.prefix_sum.append(pre_sum)

    def sumRange(self, left: int, right: int) -> int:
        pre_sum = 0
        if left != 0:
            pre_sum = self.prefix_sum[left-1]

        return self.prefix_sum[right] - pre_sum
