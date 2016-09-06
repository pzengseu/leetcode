class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path = [[0 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                path[i][j] = path[i-1][j] + path[i][j-1]

        return path[m-1][n-1]