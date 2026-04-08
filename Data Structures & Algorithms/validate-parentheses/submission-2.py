class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}' : '{'}

        # for p in s:
        #     print(stack)
        #     if p == '(' or p == '[' or p == '{':
        #         stack.append(p)
        #     elif p == ')':
        #         if len(stack) == 0 or stack.pop() != '(':
        #             return False
        #     elif p == ']':
        #         if len(stack) == 0 or  stack.pop() != '[':
        #             return False
        #     elif p == '}':
        #         if len(stack) == 0 or  stack.pop() != '{':
        #             return False
            

        # return len(stack) == 0

        for p in s:
            if p in pairs:
                if not stack or stack.pop() != pairs[p]:
                    return False
            else:
                stack.append(p)

        return not stack