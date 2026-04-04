# Problem #22: Generate Parentheses
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.9 MB
# URL        : https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()

            if openN > closeN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()
            
        backtrack(0, 0)

        return res