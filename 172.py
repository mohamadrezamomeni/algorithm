class Solution(object):
    def trailingZeroes(self, n):
        result = 0
        while n != 0:
            result += n//5
            n = n//5
        return result
