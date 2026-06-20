# Problem #295: Find Median from Data Stream
# Difficulty : Hard
# Language   : python3
# Runtime    : 1391 ms
# Memory     : 42.1 MB
# URL        : https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)

        return self.data[n // 2] if (n & 1) else ((self.data[n // 2] + self.data[n // 2 - 1]) / 2)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()