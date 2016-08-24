class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []: return []
        res = []
        self.dfs(nums, res, 0)
        return res

    def dfs(self, nums, res, pos):
        if pos == len(nums) - 1:
            res.append(nums[:])
        else:
            for i in xrange(pos, len(nums)):
                nums[pos], nums[i] = nums[i], nums[pos]
                self.dfs(nums, res, pos+1)
                nums[i], nums[pos] = nums[pos], nums[i]

print Solution().permute([1,2,3])