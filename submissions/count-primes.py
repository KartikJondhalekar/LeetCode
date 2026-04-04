# Problem #204: Count Primes
# Difficulty : Medium
# Language   : python3
# Runtime    : 195 ms
# Memory     : 53.8 MB
# URL        : https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
#         if n < 2:
#             return 0
        
#         isPrime = [True] * n
        
#         isPrime[0] = isPrime[1] = False
        
#         for i in range(2, int(n ** 0.5) + 1):
#             if isPrime[i]:
#                 for j in range(i * i, n, i):
#                     isPrime[j] = False
                    
#         return sum(isPrime)
    
        if n < 3:
            return 0

        # Only odd indices represent potential primes (2 is handled separately)
        isPrime = [True] * (n // 2)
        isPrime[0] = False  # 1 is not prime

        for i in range(3, int(n ** 0.5) + 1, 2):
            if isPrime[i // 2]:
                isPrime[i * i // 2 : n // 2 : i] = [False] * len(range(i * i // 2, n // 2, i))

        # Count primes: 1 for 2, plus number of True in odd-index array
        return sum(isPrime) + 1