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

        stack = []
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return res

                
