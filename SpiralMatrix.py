class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix: return []
        self.rec(matrix, 0, 0, len(matrix), len(matrix[0]), res)
        return res

    def rec(self, matrix, x, y, rows, cols, res):
        if rows<=0 or cols<=0: return

        #first line
        for i in xrange(cols):
            res.append(matrix[x][y + i])

        #right line
        for i in xrange(1, rows):
            res.append(matrix[x + i][y + cols - 1])

        #down line
        if rows > 1:
            for i in range(cols-1)[::-1]:
                res.append(matrix[x + rows - 1][y + i])

        #left line
        if cols > 1:
            for i in range(1, rows-1)[::-1]:
                res.append(matrix[x + i][y])

        self.rec(matrix, x+1, y+1, rows-2, cols-2, res)

    def spiralOrder2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        x1 = 0
        y1 = 0
        rows = len(matrix)
        cols = len(matrix[0])

        while rows >= 1 and cols >= 1:
            x2 = x1 + rows - 1
            y2 = y1 + cols - 1

            #go through the whole first line
            for i in range(y1, y2+1):
                res.append(matrix[x1][i])

            #go through the right column
            for i in range(x1+1, x2):
                res.append(matrix[i][y2])

            #go through the whole last row
            if rows > 1:
                for i in range(y1, y2+1)[::-1]:
                    res.append(matrix[x2][i])

            #go through the left column
            if cols > 1:
                for i in range(x1+1, x2)[::-1]:
                    res.append(matrix[i][y1])

            rows -= 2
            cols -= 2
            x1 += 1
            y1 += 1

        return res

    def spiralOrder3(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix: return res

        rows = len(matrix)
        cols = len(matrix[0])
        visitedRows = 0
        visitedCols = 0

        x = [1, 0, -1, 0]
        y = [0, 1, 0, -1]

        direct = 0
        startx = 0
        starty = 0
        candidateNum = 0
        step = 0

        while True:
            if x[direct] == 0:
                candidateNum = rows - visitedRows
            else:
                candidateNum = cols - visitedCols

            if candidateNum <= 0: break

            res.append(matrix[startx][starty])
            step += 1

            if step == candidateNum:
                step = 0
                visitedRows += 0 if x[direct] == 0 else 1
                visitedCols += 0 if y[direct] == 0 else 1

                direct += 1
                direct %= 4

            startx += y[direct]
            starty += x[direct]

        return res

print Solution().spiralOrder3([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
