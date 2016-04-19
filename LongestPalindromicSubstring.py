# -*- coding:utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        DP
        :type s: str
        :rtype: str
        """
        lens = len(s)
        start  = 0
        maxLen = 0
        table = [range(lens) for _ in xrange(lens)]
        [table[i][i] for i in xrange(lens)]
        for i in xrange(lens - 1):
            if s[i] == s[i+1]:
                table[i][i+1] = 1
                start = i
                maxLen = 2
        for leni in xrange(3, lens + 1):
            for st in xrange(lens - leni + 1):
                e = st + leni - 1
                if s[st] == s[e] and table[st+1][e-1]:
                    table[st][e]
                    start = st
                    maxLen = leni

        return s[start:start+maxLen]

    def expandAroundCenter(self, s, c1, c2):
        while c1 >= 0 and c2 <= len(s) - 1 and s[c1] == s[c2]:
            c1 -= 1
            c2 += 1
        return s[c1+1:c2]

    def longestPalindrome2(self, s):
        """
        从中间向两边展开
        :type s: str
        :rtype: str
        """
        if not s: return ''
        maxStr = s[0]
        for i in xrange(len(s) - 1):
            subStr = self.expandAroundCenter(s, i, i)
            if len(subStr) > len(maxStr):
                maxStr = subStr
            subStr = self.expandAroundCenter(s, i, i+1)
            if len(subStr) > len(maxStr):
                maxStr = subStr

        return maxStr


print Solution().longestPalindrome2("eabcb")