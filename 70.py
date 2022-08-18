class Solution:
    memory = {}

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.memory:
            return self.memory[n]
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memory[n] = result
        return result
