class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        if not strs or not strs[0]: return ''
        s = strs[0]
        for i in xrange(len(s)):
            for j in xrange(1, len(strs)):
                if len(strs[j]) < i + 1 or s[i] != strs[j][i]:
                    return res
            res += s[i]

        return res