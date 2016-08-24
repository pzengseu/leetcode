class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = range(n)
        def check(k, j):
            for i in xrange(k):
                if board[i] == j or abs(k-i) == abs(board[i]-j):
                    return False
            return True

        def dfs(depth, valueList):
            if depth == n:
                res.append(valueList[:])
                return
            for i in xrange(n):
                if check(depth, i):
                    board[depth] = i
                    dfs(depth+1, valueList+['.'*i + 'Q' + (n-i-1)*'.'])

        dfs(0, [])
        return res

print Solution().solveNQueens(4)