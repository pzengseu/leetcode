class Solution(object):
    def maximalRectangle2(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0

        maxArea = 0
        row = len(matrix)
        col = len(matrix[0])

        height = [0] * col
        left = [0] * col
        right = [col] * col

        for i in xrange(row):
            curLeft = 0
            curRight = col

            for j in xrange(col):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], curLeft)
                else:
                    height[j] = 0
                    left[j] = 0
                    curLeft = j + 1

            for j in xrange(col-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curRight)
                else:
                    right[j] = col
                    curRight = j

                maxArea = max(maxArea, height[j] * (right[j] - left[j]))

        return maxArea

    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]: return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0

        for row in matrix:
            for i in xrange(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0

            stack = [-1]
            for i in xrange(n+1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)

                stack.append(i)

        return ans

