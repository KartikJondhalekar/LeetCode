# Problem #67: Add Binary
# Difficulty : Easy
# Language   : python3
# Runtime    : 3 ms
# Memory     : 16.8 MB
# URL        : https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []

        # Start from the last index of both strings
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            # Get current digits or 0 if out of bounds
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum and carry
            total = digit_a + digit_b + carry
            carry = total // 2
            result.append(str(total % 2))  # Append the current bit
            
            # Move to the next most significant digit
            i -= 1
            j -= 1

        # Join and reverse result in one step
        return ''.join(result[::-1])
