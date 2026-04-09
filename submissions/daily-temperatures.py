# Problem #739: Daily Temperatures
# Difficulty : Medium
# Language   : python3
# Runtime    : 107 ms
# Memory     : 28.6 MB
# URL        : https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # Brute Force
        # res = [0] * len(temperatures)

        # for i in range(len(temperatures) - 1):
        #     curr_temp = temperatures[i]
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > curr_temp:
        #             res[i] = j - i
        #             break

        # return res

        pending_days = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while pending_days and temp > temperatures[pending_days[-1]]:
                res[pending_days[-1]] = i - pending_days[-1]
                pending_days.pop()
            pending_days.append(i)

        return res