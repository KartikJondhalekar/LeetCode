# Problem #678: Valid Parenthesis String
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.1 MB
# URL        : https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0