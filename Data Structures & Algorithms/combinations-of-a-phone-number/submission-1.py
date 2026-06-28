class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digiMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }

        def backtrack(i, combination):
            if len(combination) == len(digits):
                res.append(combination[:])
                return

            for c in digiMap[digits[i]]:
                backtrack(i + 1, combination + c)

        if digits:
            backtrack(0, "")

        return res