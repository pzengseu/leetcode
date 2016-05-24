class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        size = len(board)
        for i in xrange(size):
            s1 = set()
            num1 = 0
            s2 = set()
            num2 = 0
            for j in xrange(size):
                if board[i][j] == '.':
                    num1 += 1
                else: s1.add(board[i][j])

                if board[j][i] == '.':
                    num2 += 1
                else: s2.add(board[j][i])
            if len(s1) != size - num1: return False
            if len(s2) != size - num2: return False

        m = size / 3
        for i in xrange(m*m):
            s = set()
            num = 0
            for j in xrange(3):
                for k in xrange(3):
                    if board[(i/3)*3+j][(i%3)*3+k] == '.':
                        num += 1
                    else: s.add(board[(i/3)*3+j][(i%3)*3+k])

            if len(s) != 9 - num: return False


        return True

print Solution().isValidSudoku(["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"])