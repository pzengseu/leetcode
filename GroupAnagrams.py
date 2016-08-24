class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        d = {}
        for s in strs:
            temp = ''.join(sorted(s))
            if temp in d:
                d[temp].append(s)
            else:
                d[temp] = [s]
                # d[temp].append(s)

        for k in d:
            res.append(d[k])

        return res

print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])