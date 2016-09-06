class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * n
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        res[0] = 1
        res[1] = 2
        for i in xrange(2, n):
            res[i] = res[i-1]+res[i-2]

        return res[-1]