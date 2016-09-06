class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        path = [[ 1 for i in xrange(n)] for j in xrange(m)]

        if obstacleGrid[0][0]: return 0
        if obstacleGrid[m-1][n-1]: return 0
        for i in xrange(1, n):
            if obstacleGrid[0][i-1]:
                path[0][i] = 0
            else:
                path[0][i] = path[0][i-1]

        for j in xrange(1, m):
            if obstacleGrid[j-1][0]:
                path[j][0] = 0
            else:
                path[j][0] = path[j-1][0]

        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i-1][j] and obstacleGrid[i][j-1]:
                    path[i][j] = 0
                elif not obstacleGrid[i-1][j] and obstacleGrid[i][j-1]:
                    path[i][j] = path[i-1][j]
                elif obstacleGrid[i-1][j] and not obstacleGrid[i][j-1]:
                    path[i][j] = path[i][j-1]
                else:
                    path[i][j] = path[i-1][j] + path[i][j-1]

        return path[m-1][n-1]

print Solution().uniquePathsWithObstacles([[0,1]])