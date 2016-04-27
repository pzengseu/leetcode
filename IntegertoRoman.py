class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ''
        for i in xrange(len(values)):
            while num >= values[i]:
                res += symbols[i]
                num -= values[i]
        return res

    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        pre = d[s[0]]
        res += pre
        for i in xrange(1, len(s)):
            if d[s[i]] <= pre: res += d[s[i]]
            else: res = res + d[s[i]] - 2 * pre
            pre = d[s[i]]
        return res
