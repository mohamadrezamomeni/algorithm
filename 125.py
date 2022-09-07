import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        s = s.lower()
        lowers = string.ascii_lowercase
        alphanumeric = lowers + '1234567890'
        for c in s:
            if c in alphanumeric:
                result += c

        return result == result[::-1]
