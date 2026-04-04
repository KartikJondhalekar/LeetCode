# Problem #9: Palindrome Number
# Difficulty : Easy
# Language   : python3
# Runtime    : 62 ms
# Memory     : 17.4 MB
# URL        : https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num = x
        new_num = 0

        while x > 0:
            new_num = new_num * 10 + x % 10
            x = x // 10
        
        return new_num == num