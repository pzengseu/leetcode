class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if x <= 2: return 1
        left = 0
        right = x / 2 + 1
        while left <= right:
            mid = (left + right) / 2
            sq = mid * mid
            if sq == x: return mid
            elif sq < x: left = mid + 1
            else: right = mid - 1

        return right

print Solution().mySqrt(0)