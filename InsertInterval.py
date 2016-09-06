class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        if not intervals:
            res.append(newInterval)
            return res

        pos = 0
        while pos < len(intervals) and intervals[pos].end < newInterval.start:
            res.append(intervals[pos])
            pos += 1

        res.append(newInterval)
        while pos < len(intervals) and res[-1].end >= intervals[pos].start:
            res[-1].start = min(res[-1].start, intervals[pos].start)
            res[-1].end = max(res[-1].end, intervals[pos].end)
            pos += 1

        while pos < len(intervals):
            res.append(intervals[pos])

        return res
