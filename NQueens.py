class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        if n == 0: return res
        self.dfs(range(n), res, 0)
        return res

    def dfs(self, nums, res, pos):
        if pos == len(nums) - 1:
            if self.check(nums):
                res.append(self.printQ(nums[:]))
        else:
            for i in xrange(pos, len(nums)):
                nums[i], nums[pos] = nums[pos], nums[i]
                self.dfs(nums, res, pos+1)
                nums[i], nums[pos] = nums[pos], nums[i]

    def check(self, nums):
        for i in xrange(len(nums)-1):
            for j in xrange(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == abs(i - j):
                    return False
        return True

    def printQ(self, nums):
        tmp = []
        n = len(nums)
        for i in nums:
            tmp.append('.'*i + 'Q' + (n-i-1)*'.')
        return tmp

print Solution().solveNQueens(9)