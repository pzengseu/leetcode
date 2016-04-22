class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        j = len(height) - 1
        while i < j:
            res = max(res, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                temp = height[i]
                while i < j:
                    i += 1
                    if height[i] > temp:
                        break
                continue
            else:
                temp = height[j]
                while i < j:
                    j -= 1
                    if height[j] > temp:
                        break
                continue

        return res

    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        j = len(height) - 1
        while i < j:
            res = max(res, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]: i += 1
            else: j -= 1

        return res

print Solution().maxArea2([1,1])