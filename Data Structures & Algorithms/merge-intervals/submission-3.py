class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort()
        res = []
        newInterval = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                newInterval = intervals[i]
            else:
                newInterval[1] = max(newInterval[1], intervals[i][1])

        res.append(newInterval)

        return res