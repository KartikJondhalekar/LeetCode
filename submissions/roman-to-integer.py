# Problem #13: Roman to Integer
# Difficulty : Easy
# Language   : python3
# Runtime    : 9 ms
# Memory     : 17.8 MB
# URL        : https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        # res = 0
        # for i in range(len(s)):
        #     if s[i] == 'M':
        #         if i > 0 and s[i - 1] == 'C':
        #             res += 800
        #         else:
        #             res += 1000
        #     elif s[i] == 'D':
        #         if i > 0 and s[i - 1] == 'C':
        #             res += 300
        #         else:
        #             res += 500
        #     elif s[i] == 'C':
        #         if i > 0 and s[i - 1] == 'X':
        #             res += 80 
        #         else:
        #             res += 100
        #     elif s[i] == 'L':
        #         if i > 0 and s[i - 1] == 'X':
        #             res += 30 
        #         else:
        #             res += 50
        #     elif s[i] == 'X':
        #         if i > 0 and s[i - 1] == 'I':
        #             res += 8 
        #         else:
        #             res += 10
        #     elif s[i] == 'V':
        #         if i > 0 and s[i - 1] == 'I':
        #             res += 3
        #         else: 
        #             res += 5
        #     elif s[i] == 'I':
        #         res += 1
        
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
                
        return res