class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for v in nums:
            if v != val:
                nums[i] = v
                i += 1

        return len(nums[:i])

    def removeElement2(self, nums, val):
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1

        return n
print Solution().removeElement([3,2,2,3], 3)