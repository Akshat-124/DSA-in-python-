class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        n = x
        result = 0
        while n > 0:
            ld = n % 10          
            result = (result * 10) + ld
            n = n // 10          
        return x == result
        