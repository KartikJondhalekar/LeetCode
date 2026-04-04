# Problem #412: Fizz Buzz
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 18.3 MB
# URL        : https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        for i in range(1, n + 1):
            div3 = ((i % 3) == 0)
            div5 = ((i % 5) == 0)
            
            if div3 and div5:
                answer.append("FizzBuzz")
            elif div3:
                answer.append("Fizz")
            elif div5:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        
        return answer