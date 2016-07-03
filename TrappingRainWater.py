class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        res = 0
        maxh = 0
        for i in xrange(1, len(height)):
            if height[i] > height[maxh]:
                maxh = i

        lh = 0
        for i in xrange(maxh):
            if height[i] > lh:
                lh = height[i]
            else:
                res += (lh - height[i])

        rh = 0
        for i in range(maxh, len(height))[::-1]:
            if height[i] > rh:
                rh = height[i]
            else:
                res += (rh - height[i])

        return res

print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
