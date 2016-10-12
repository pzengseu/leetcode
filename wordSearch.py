class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.check(board, i, j, word, 0): return True
        return False

    def check(self, board, i, j, word, index):
        if index == len(word): return True
        if i > len(board)-1 or i < 0 or j < 0 or j > len(board[0]) - 1 or \
                        board[i][j] != word[index]:
            return False
        board[i][j] = '*'
        result = self.check(board, i, j + 1 ,word, index+1) or \
                 self.check(board, i, j - 1, word, index+1) or \
                 self.check(board, i + 1, j, word, index+1) or \
                 self.check(board, i - 1, j, word, index+1)
        board[i][j] = word[index]

        return result

if __name__ == '__main__':
    s = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    print Solution().exist(s, 'SEECFA')
