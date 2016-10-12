class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        while i < n:
            if matrix[i][0] > target:
                break
            i += 1

        for j in xrange(n):
            if matrix[i-1][j] == target:
                return True

        return False
