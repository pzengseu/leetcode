class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for i in range(n)]
        if n == 0: return []

        j = 1
        x1 = 0
        y1 = 0
        rows = n
        cols = n

        while j <= n*n :
            x2 = x1 + cols - 1
            y2 = y1 + rows - 1

            for i in range(x1, x2 + 1):
                res[y1][i] = j
                j += 1

            for i in range(y1 + 1, y2):
                res[i][x2] = j
                j += 1

            if rows > 1:
                for i in range(x1, x2 + 1)[::-1]:
                    res[y2][i] = j
                    j += 1

            if cols > 1:
                for i in range(y1 + 1, y2)[::-1]:
                    res[i][x1] = j
                    j += 1

            rows -= 2
            cols -= 2
            x1 += 1
            y1 += 1

        return res

print Solution().generateMatrix(4)