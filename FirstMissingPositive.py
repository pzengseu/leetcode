class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] != i+1 and nums[i] <= l and nums[i] > 0 and nums[i] != nums[nums[i] - 1]:
                # print nums
                # print nums[i]
                # print nums[nums[i] - 1]
                t = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[t - 1] = t
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                # print nums
                # print '-------------'
            else:
                print i
                i += 1

        for j in xrange(l):
            if nums[j] != j + 1:
                return j + 1

        return l + 1

print Solution().firstMissingPositive([1])