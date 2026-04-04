# Problem #17: Letter Combinations of a Phone Number
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.8 MB
# URL        : https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        LETTERS = {'2': "abc",
                   '3': "def",
                   '4': "ghi",
                   '5': "jkl",
                   '6': "mno",
                   '7': "pqrs",
                   '8': "tuv",
                   '9': "wxyz"}
        
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return

            for c in LETTERS[digits[i]]:
                backtrack(i + 1, currStr + c)

        if digits:
            backtrack(0, "")
                                           
        return res