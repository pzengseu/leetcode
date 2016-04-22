class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        if not x:
            return True
        y = int(str(x)[::-1])
        if y == abs(x): return True
        return False

    def isPalindrome(self, x):
        if x < 0: return False
        xx = x
        y = 0
        while x:
            y = y * 10 + x % 10
            x /= 10
        if xx == y: return True
        else: return False

print Solution().isPalindrome(1)