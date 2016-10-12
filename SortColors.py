class Solution(object):
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)-1):
            for j in xrange(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    def sortColors(self, nums):
        i = -1
        j = -1
        k = -1
        for n in nums:
            if n == 0:
                i += 1
                j += 1
                k += 1
                nums[k] = 2
                nums[j] = 1
                nums[i] = 0

            if n == 1:
                j += 1
                k += 1
                nums[k] = 2
                nums[j] = 1

            if n == 2:
                k += 1
                nums[k] = 2



