class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = '1'
        for i in xrange(1, n):
            ret = self.solution(ret)

        return ret

    def solution(self, s):
        ret = ''
        count = 1
        pre = s[0]
        for i in xrange(1,len(s)):
            if s[i] == pre:
                count += 1
            else:
                ret = ret + str(count) + pre
                count = 1
                pre = s[i]
        ret = ret + str(count) + pre
        return ret

print Solution().countAndSay(8)