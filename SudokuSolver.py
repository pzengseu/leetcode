class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in xrange(len(board)):
            board[i] = list(board[i])
        self.solve(board)
        for i in xrange(len(board)):
            board[i] = ''.join(board[i])

    def solve(self, board):
        for row in xrange(9):
            for col in xrange(9):
                if board[row][col] == '.':
                    for i in xrange(1, 10):
                        board[row][col] = str(i)
                        if self.isVaild(board, row, col) and self.solve(board):
                            return True
                        board[row][col] = '.'
                    return False
        return True

    def isVaild(self, board, row, col):
        for i in xrange(9):
            if i != col and board[row][i] == board[row][col]:
                return False

        for i in xrange(9):
            if i != row and board[i][col] == board[row][col]:
                return False

        beginRow = (row / 3) * 3
        beginCol = (col / 3) * 3
        for i in xrange(beginRow, beginRow+3):
            for j in xrange(beginCol, beginCol+3):
                if i != row and j != col and board[i][j] == board[row][col]:
                    return False
        return True

print Solution().solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])