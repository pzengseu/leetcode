class Solution(object):
    def recursion(self, left, right, ps, res):
        if not left and not right:
            res.append(ps)
            return
        if left > 0:
            self.recursion(left-1, right, ps+'(', res)
        if right > left:
            self.recursion(left, right-1, ps+')', res)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.recursion(n, n, '', res)
        return res
