# Problem #150: Evaluate Reverse Polish Notation
# Difficulty : Medium
# Language   : python3
# Runtime    : 3 ms
# Memory     : 20.7 MB
# URL        : https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(token))

        return stack.pop()