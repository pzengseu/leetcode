class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hlen = len(haystack)
        nlen = len(needle)

        i = 0
        j = 0
        while i < hlen and j < nlen:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0

        if j == nlen: return i-j
        return -1
