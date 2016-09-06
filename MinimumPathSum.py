class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        path =[grid[j][:] for j in xrange(m)]

        if not m and not n: return 0

        if m == 1 and n == 1:
            return grid[0][0]
        for i in xrange(1, n):
            path[0][i] += path[0][i-1]

        for j in xrange(1, m):
            path[j][0] += path[j-1][0]

        for i in xrange(1, m):
            for j in xrange(1, n):
                path[i][j] = min(path[i][j]+path[i-1][j], path[i][j]+path[i][j-1])

        return path[m-1][n-1]

print Solution().minPathSum([[1,2],[1,1]])