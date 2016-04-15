class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return sorted([i, j])

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = {}
        for i in xrange(len(nums)):
            if (target - nums[i]) in numsDict:
                return [numsDict[target - nums[i]], i]
            numsDict[nums[i]] = i

s = Solution()
print s.twoSum2([0,4,3,0], 0)