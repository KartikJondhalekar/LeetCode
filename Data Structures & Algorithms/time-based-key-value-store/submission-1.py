class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key][0].append(value)
            self.timeMap[key][1].append(timestamp)
        else:
            self.timeMap[key] = [[value], [timestamp]]        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        timestamps = self.timeMap[key][1]
        values = self.timeMap[key][0]

        l, r = 0, len(timestamps) - 1

        while l <= r:
            mid = (l + r) // 2

            if timestamps[mid] == timestamp:
                return values[mid]
            elif timestamps[mid] > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        return values[r] if r >= 0 else ""