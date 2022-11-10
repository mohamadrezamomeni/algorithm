class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memory = {}

        def min_cost(n):
            if n == 0:
                return cost[n]
            if n == 1:
                return cost[n]

            if n in memory:
                return memory[n]

            result = min(min_cost(n-1), min_cost(n-2)) + cost[n]
            memory[n] = result
            return result
        cost_len = len(cost)
        return min(min_cost(cost_len-1), min_cost(cost_len-2))
