class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        if not intervals: return res
        intervals.sort(key=lambda x:x.start)

        res.append(intervals[0])
        for i in xrange(1, len(intervals)):
            if res[-1].end >= intervals[i].start:
                res[-1].end = max(intervals[i].end, res[-1].end)
            else:
                res.append(intervals[i])

        return res
