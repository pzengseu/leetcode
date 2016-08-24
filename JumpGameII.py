class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #DP
        if len(nums) <= 1: return 0
        dp = [10**5] * len(nums)
        dp[0] = 0

        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[j] + j >= i:
                    if dp[j] + 1 < dp[i]:
                        dp[i] = dp[j] + 1
                        break

        return dp[-1]

    #greedy
    def jump2(self, nums):
        last_max_reach, current_max_reach = 0, 0
        njump, i = 0, 0

        while current_max_reach < len(nums) -1:
            while i <= last_max_reach:
                current_max_reach = max(i+nums[i], current_max_reach)
                i += 1
            last_max_reach = current_max_reach
            njump += 1

        return njump


print Solution().jump2([2,3,1,1,4])