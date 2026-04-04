class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = dict()

        for char in s:
            chars[char] = chars.get(char, 0) + 1

        for char in t:
            if char not in chars:
                return False
            chars[char] -= 1
        
        return all(count == 0 for count in chars.values())