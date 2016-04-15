class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 1
        if not s: return 0
        i = 0
        temp = 1
        while i < len(s) and temp:
            ws = {}
            ws[s[i]] = i
            ifBreak = False
            for j in xrange(i+1, len(s)):
                if s[j] in ws:
                    i = ws[s[j]] + 1
                    ifBreak = True
                    break
                ws[s[j]] = j
                if j - i + 1 > m:
                    m = j - i + 1
                if j == len(s):
                    temp = 0
            if not ifBreak:
                i += 1
        return m

    def lengthOfLongestSubstring2(self, s):
        ws = {}
        m = 0
        left = -1
        for i in xrange(len(s)):
            if s[i] in ws and ws[s[i]] > left:
                left = ws[s[i]]
            ws[s[i]] = i
            m = i - left if i - left > m else m
        return m

print Solution().lengthOfLongestSubstring2("abba")