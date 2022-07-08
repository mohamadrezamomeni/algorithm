class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if int(str(x)[::-1]) == x:
            return True
        return False
