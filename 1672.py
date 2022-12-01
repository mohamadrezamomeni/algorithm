class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for account in accounts:
            max_sum = max(sum(account), max_sum)
        return max_sum
