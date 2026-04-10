class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        st = ""

        for c in s:
            if c.isalnum():
                st += c

        i, j = 0, len(st) - 1

        while i < j:
            if st[i] != st[j]:
                return False

            i += 1
            j -= 1

        return True        