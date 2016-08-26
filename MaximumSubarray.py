class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[-1]
        maxsum = sum
        for i in range(len(nums)-1)[::-1]:
            sum = max(nums[i], nums[i] + sum)
            maxsum = max(sum, maxsum)

        return maxsum

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        maxsum = sum
        for i in range(1, len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]
            maxsum = max(sum, maxsum)

        return maxsum

    def maxSubArray3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.divideNConquer(nums, 0, len(nums)-1)

    def divideNConquer(self, nums, l, r):
        if l == r: return nums[l]

        m = (l + r) / 2
        left = self.divideNConquer(nums, l, m)
        right = self.divideNConquer(nums, m+1, r)
        middle = nums[m]
        tmp = middle
        for i in range(l, m)[::-1]:
            tmp += nums[i]
            middle = max(tmp, middle)
        tmp = middle
        for j in range(m+1, r+1):
            tmp += nums[j]
            middle = max(tmp, middle)

        return max(middle, max(left, right))

print Solution().maxSubArray3([-2,1,-3,4,-1,2,1,-5,4])
