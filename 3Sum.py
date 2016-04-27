class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        nums = sorted(nums)
        res = []
        for i in xrange(len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append((nums[i], nums[j], nums[k]))
                if nums[i] + nums[j] + nums[k] < 0: j += 1
                else: k -= 1

        return [list(l) for l in {}.fromkeys(res).keys()]
print Solution().threeSum([12,-14,-5,12,-2,9,0,9,-3,-3,-14,-6,-4,13,-11,-8,0,5,-7])