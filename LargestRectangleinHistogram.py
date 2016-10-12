class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = []

        i = 0
        while i <= len(heights):
            h = (0 if i == len(heights) else heights[i])

            if not stack or h >= heights[stack[-1]]:
                stack.append(i)
            else:
                # print stack
                tp = stack.pop()
                # print tp
                maxArea = max(maxArea, heights[tp] * (i if not stack else i - stack[-1] - 1))
                # print maxArea
                i -= 1
            i += 1

        return maxArea

if __name__ == '__main__':
    print Solution().largestRectangleArea([2,1,5,6,2,3])