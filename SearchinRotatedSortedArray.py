class Solution(object):
    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        while index < len(nums)-1 and nums[index] < nums[index+1]:
            index += 1

        if index == len(nums)-1:
            if nums[0] <= target <=nums[-1]:
                i = 0
                while i < len(nums):
                    if nums[i] == target:
                        return i
                    i += 1
            else:
                return -1

            return -1

        if nums[index + 1] <= target <= nums[index]:
            if target >= nums[0]:
                i = 0
                while i <= index:
                    if nums[i] == target:
                        return i
                    i += 1
            if target <= nums[-1]:
                i = index + 1
                while i < len(nums):
                    if nums[i] == target:
                        return i
                    i += 1
        else:
            return -1

        return -1

    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if nums[m] == target: return m

            if nums[l] < nums[r]:
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] >= nums[l]:
                    if target > nums[m] or target < nums[l]:
                        l = m + 1
                    else: r = m - 1
                elif nums[m] < nums[l]:
                    if target < nums[m] or target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1

        if nums[l] == target: return l
        return -1


print Solution().search([3, 1], 1)


