class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.myCombine(n, k, 1, [], res)

        return res

    def myCombine(self, n, k, start, temp, res):
        if len(temp) == k:
            res.append(temp[:])
            return

        for i in xrange(start, n+1):
            temp.append(i)
            self.myCombine(n, k, i+1, temp, res)
            del temp[-1]

print Solution().combine(4, 3)