class Solution(object):
    # time limited
    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        res = 1.0
        for i in xrange(abs(n)):
            res *= x
            if abs(res) < 0.00000001: return 0

        if n < 0: return 1.0/res
        return res

    def myPow(self, x, n):
        if n < 0:
            return 1.0 / self.power(x, -n)
        else:
            return self.power(x, n)

    def power(self, x, n):
        if n == 0: return 1

        tmp = self.power(x, n / 2)
        if n & 0x01 == 1: return tmp * tmp * x
        else: return tmp * tmp