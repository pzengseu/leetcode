class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]

        for i in xrange(len(nums)):
            for j in xrange(len(result)):
                subSet = result[j][:]
                subSet.append(nums[i])
                result.append(subSet)

        return result

    def subsets2(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)

print Solution().subsets2([1,2,3])