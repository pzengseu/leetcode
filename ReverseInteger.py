class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        temp = 0 if x > 0 else 1
        x = x if x > 0 else -x
        while x:
            t = x % 10
            x /= 10
            res = res * 10 + t
        if res > 2 ** 31:
            return 0
        if temp: return -res
        return res

    def reverse2(self, x):
        res = int(str(abs(x))[::-1])
        if res > 2 ** 31:
            return 0
        return res * cmp(x, 0)

print Solution().reverse(-321)