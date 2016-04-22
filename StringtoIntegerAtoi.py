class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        sign = 1
        s = str.strip()
        for i in xrange(len(s)):
            c = s[i]
            if not c:
                return res
            if c == '+' and not i:
                sign = 1
                continue
            if c == '-' and not i:
                sign = -1
                continue
            if -1 < ord(c) - 48 < 10: res = res * 10 + ord(c) - 48
            else: break

        res *= sign
        if res > 2 ** 31 - 1: return 2 ** 31 - 1
        if res < -2 ** 31: return -2 ** 31
        return res

