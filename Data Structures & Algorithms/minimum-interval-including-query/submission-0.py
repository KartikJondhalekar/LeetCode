class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        shortest = []
        print(intervals)
        intervals.sort()
        print(intervals)

        for query in queries:
            for i in range(len(intervals)):
                if query in range(intervals[i][0], intervals[i][1] + 1):
                    if len(shortest) == 0:
                        shortest.append((intervals[i][0], intervals[i][1]))
                    elif len(shortest) != 0 and (intervals[i][1] - intervals[i][0]) < (shortest[0][1] - shortest[0][0]):
                        shortest.pop()
                        shortest.append((intervals[i][0], intervals[i][1]))
            
            if len(shortest) == 0:
                res.append(-1)
            else:
                start, end = shortest.pop()
                res.append(end - start + 1)

        return res