class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        self.backTracking([], 0, target, ret, candidates)
        return ret

    def backTracking(self, cur, start, target, ret, can):
        if target == 0:
            temp = cur[:]
            if temp not in ret: ret.append(temp)
        else:
            i = start
            while i < len(can) and can[i] <= target:
                cur.append(can[i])
                self.backTracking(cur, i + 1, target - can[i], ret, can)
                del cur[-1]
                i += 1