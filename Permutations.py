class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []: return []
        res = []
        self.dfs(nums, [False] * len(nums), [], res)
        return res

    def dfs(self, nums, used, item, res):
        if len(item) == len(nums):
            res.append(item[:])
            return

        for i in xrange(len(nums)):
            if not used[i]:
                used[i] = True
                item.append(nums[i])
                self.dfs(nums, used, item, res)
                del item[-1]
                used[i] = False

print Solution().permute([1,2,3])