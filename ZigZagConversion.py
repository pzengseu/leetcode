class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        resD = [[] for _ in xrange(numRows)]
        lenEach = 2 * numRows - 2
        for i in xrange(len(s)):
            t = i % lenEach if i % lenEach < numRows - 1 else (lenEach - i % lenEach)
            resD[t].append(s[i])
        return ''.join(reduce(lambda x,y: x+y, resD))

print Solution().convert("PAYPALISHIRING", 3)