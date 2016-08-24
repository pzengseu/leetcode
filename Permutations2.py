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
            nums = nums[:pos] + sorted(nums[pos:])
            for i in xrange(pos, len(nums)):
                if i != pos and nums[i] == nums[i-1]:
                    continue
                nums[pos], nums[i] = nums[i], nums[pos]
                self.dfs(nums, res, pos+1)
                nums[i], nums[pos] = nums[pos], nums[i]

print Solution().permute([1,1,2,3])