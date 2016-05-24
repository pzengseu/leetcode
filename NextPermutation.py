class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        size = len(nums)

        index = size - 1
        while index > 0 and nums[index] <= nums[index - 1]:
            index -= 1

        if not index:
            nums.sort()
            return

        exchangeIndex = size - 1
        while nums[exchangeIndex] <= nums[index - 1]:
            exchangeIndex -= 1

        nums[index - 1], nums[exchangeIndex] = nums[exchangeIndex], nums[index - 1]
        nums[index:] = sorted(nums[index:])