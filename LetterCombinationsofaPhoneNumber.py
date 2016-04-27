import Queue
class Solution(object):
    def rec(self, digits, initMap, res, cache):
        if not digits:
            res.append(cache)
            return
        s = initMap[int(digits[0])]
        for i in xrange(len(s)):
            cache += s[i]
            self.rec(digits[1:], initMap, res, cache)
            cache = cache[:-1]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        initMap = ['', '', "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        self.rec(digits, initMap, res, '')
        return res

    def letterCombinationsQ(self, digits):
        res = []
        if not digits: return []
        initMap = ['', '', "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        q = Queue.Queue()
        s = initMap[int(digits[0])]
        [q.put(s[i]) for i in xrange(len(s))]
        index = 1
        while not q.empty():
            size = q.qsize()
            for i in xrange(size):
                temp = q.get()
                if index < len(digits):
                    tempS = initMap[int(digits[index])]
                    [q.put(temp + tempS[k]) for k in xrange(len(tempS))]
                else: res.append(temp)
            index += 1

        return res

print Solution().letterCombinationsQ("23")