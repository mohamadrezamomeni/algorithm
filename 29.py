class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negetive = (dividend > 0 and divisor < 0) or (
            dividend < 0 and divisor > 0)

        if divisor in [-1, 1]:
            if negetive:
                return min(abs(dividend), 2147483648)*-1
            else:
                return min(abs(dividend), 2147483647)

        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0

        list_divisor = [divisor]
        while dividend - divisor >= 0:
            l = len(list_divisor)
            for i, v in enumerate(list_divisor[::-1]):
                if dividend - v >= 0:
                    count += (2**(l - i - 1))
                    dividend -= v
                    if i == 0:
                        list_divisor.append(v*2)
                    break

        if negetive:
            return min(count, 2147483648)*-1
        else:
            return min(count, 2147483647)
