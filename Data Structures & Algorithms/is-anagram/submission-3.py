class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = []

        source = s if (len(s) >= len(t)) else t
        target = t if (len(s) >= len(t)) else s

        for char in source:
            chars.append(char)

        for char in target:
            if char in chars:
                chars.remove(char)

        return len(chars)==0