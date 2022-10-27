class Solution:
    def isUgly(self, n: int) -> bool:
        primes = [2, 3, 5]
        if n in primes:
            return True
        if n == 1:
            return True
        if n <= 0:
            return False

        def divide(num):
            for prime in primes:
                result = num/prime
                if result == 1:
                    return True
                elif result.is_integer():
                    return divide(num/prime)
            return False
        return divide(n)
