import Queue
class Solution(object):
    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        sindex = 0
        stack = Queue.LifoQueue()

        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.put(i)
            else:
                if stack.empty():
                    sindex = i + 1
                else:
                    stack.get()
                    if stack.empty(): ret = max(ret, i - sindex + 1)
                    else:
                        sindex2 = stack.get()
                        ret = max(ret, i - sindex2)
                        stack.put(sindex2)
            i += 1

        return ret

    def longestValidParentheses(self, s):
        size = len(s)
        if size < 2: return 0
        max = 0
        dp = [0] * size

        for i in range(size-1)[::-1]:
            if s[i] == '(':
                j = i + 1 + dp[i+1]
                if j < size and s[j] == ')':
                    dp[i] = dp[i+1] + 2
                    if j+1 < size:
                        dp[i] += dp[j+1]
                if dp[i] > max:
                    max = dp[i]

        return max

print Solution().longestValidParentheses("(()()")