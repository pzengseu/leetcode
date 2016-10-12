class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) / 2
            if nums[m] == target: return True
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else: l += 1

        return False

if __name__ == '__main__':
    print Solution().search([1,1,5,1,1,1,1], 5)