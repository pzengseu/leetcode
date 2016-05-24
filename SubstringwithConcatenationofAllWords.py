class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ret = []
        if not len(s) or not words: return []

        size = len(words[0])
        target = {}
        for w in words:
            if w in target: target[w] += 1
            else: target[w] = 1

        for i in xrange(size):
            b = i
            cnt = 0
            j = i
            temp = {}
            while j + size <= len(s):
                subStr = s[j: j + size]
                if subStr in target:
                    if subStr in temp: temp[subStr] += 1
                    else: temp[subStr] = 1
                    cnt += 1

                    while temp[subStr] > target[subStr]:
                        temp[s[b: b+size]] -= 1
                        cnt -= 1
                        b += size

                    if cnt == len(words):
                        temp[s[b: b+size]] -= 1
                        ret.append(b)
                        cnt -= 1
                        b += size
                else:
                    b = j + size
                    temp.clear()
                    cnt = 0

                j += size

        return ret

print Solution().findSubstring("barfoofoobarthefoobarman",["bar","foo","the"])



