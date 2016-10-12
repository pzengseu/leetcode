class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        isRowZero = False
        isColZero = False

        for i in xrange(m):
            if matrix[i][0] == 0:
                isRowZero = True
                break

        for j in xrange(n):
            if matrix[0][j] == 0:
                isColZero = True
                break

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in xrange(1, m):
            if matrix[i][0] == 0:
                for j in xrange(1, n):
                    matrix[i][j] = 0

        for j in xrange(n):
            if matrix[0][j] == 0:
                for i in xrange(1, m):
                    matrix[i][j] = 0

        if isRowZero:
            for i in xrange(m):
                matrix[i][0]=0

        if isColZero:
            for j in xrange(n):
                matrix[0][j]=0

        return matrix

print Solution().setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])