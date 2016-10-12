class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mHash = {}
        for i in t:
            if i in mHash:
                mHash[i] += 1
            else:
                mHash[i] = 1

        cnt = 0
        l = 0
        minl = 0
        minsize = len(s) + 1

        for r in xrange(len(s)):
            if s[r] in mHash:
                mHash[s[r]] -= 1
                if mHash[s[r]] >= 0: cnt += 1

            while cnt == len(t):
                if r - l + 1 < minsize:
                    minl = l
                    minsize = r - l + 1
                if s[l] in mHash:
                    mHash[s[l]] += 1
                    if mHash[s[l]] > 0:
                        cnt -= 1

                l += 1

        if minsize > len(s): return ''
        return s[minl:(minl + minsize)]


print Solution().minWindow("ADOBECODEBANC", "ABC")
