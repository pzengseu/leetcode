class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums): return 0
        n = 0
        for i in xrange(len(nums)):
            if nums[n] != nums[i]:
                n += 1
                nums[n] = nums[i]
        return n+1

print Solution().removeDuplicates([1,1,1,3])