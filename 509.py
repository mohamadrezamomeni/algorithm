class Solution:
    memory = {}

    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        if n in self.memory:
            return self.memory[n]
        result = self.fib(n - 1) + self.fib(n - 2)
        self.memory[n] = result
        return result
