class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1

        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1

            while j > 0 and not s[j].isalnum() :
                j -= 1

            if i < j and s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True        