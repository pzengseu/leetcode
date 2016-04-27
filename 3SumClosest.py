class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return []
        diffSub = 2 ** 31
        res = target
        nums = sorted(nums)
        res = []
        for i in xrange(len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k] - target
                if not temp: return target
                if abs(temp) < diffSub:
                    diffSub = abs(temp)
                    res = nums[i] + nums[j] + nums[k]
                if temp < 0: j += 1
                else: k -= 1

        return res

print Solution().threeSumClosest([0,1,2], 0)
