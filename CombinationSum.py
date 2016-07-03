class Solution(object):
    def combinationSum(self, candidates, target):
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
            # temp = cur[:]
            ret.append(cur[:])
        else:
            i = start
            while i < len(can) and can[i] <= target:
                cur.append(can[i])
                self.backTracking(cur, i, target - can[i], ret, can)
                del cur[-1]
                i += 1

print Solution().combinationSum([2,3,6,7], 7)