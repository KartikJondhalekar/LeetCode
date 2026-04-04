# Problem #20: Valid Parentheses
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 18.1 MB
# URL        : https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        para = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for p in s:
            if p in para:
                stack.append(para[p])
            else:
                if not stack or stack.pop() != p:
                    return False

        return len(stack) == 0