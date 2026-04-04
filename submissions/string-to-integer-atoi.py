# Problem #8: String to Integer (atoi)
# Difficulty : Medium
# Language   : python3
# Runtime    : 3 ms
# Memory     : 17.7 MB
# URL        : https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        s = s.strip()        
        n = len(s)
        start = 0
        res = 0
        
        if n >= 1 and s[0] == "-":
            start = 1
            neg = True
        elif n >= 1 and s[0] == "+":
            start = 1
                
        for i in range(start, n):
            if (s[i] >= '0' and s[i] <= '9'):
                res = res * 10 + int(s[i])
            else:
                break
        
        res = -res if neg else res 
        
        if res > 2**31 - 1:
            return 2**31 - 1
        elif res < -2**31:
            return -2**31
        
        return res
            
        