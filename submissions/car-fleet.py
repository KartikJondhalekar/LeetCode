# Problem #853: Car Fleet
# Difficulty : Medium
# Language   : python3
# Runtime    : 243 ms
# Memory     : 40.3 MB
# URL        : https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pairs = sorted([[p, s] for p, s in zip(position, speed)], reverse = True)
        pairs = [[p, s] for p, s in zip(position, speed)]

        eta_stack = []

        # for p, s in pairs:
        for p, s in sorted(pairs)[::-1]:
            eta_stack.append((target - p) / s)
            if len(eta_stack) >= 2 and eta_stack[-1] <= eta_stack[-2]:
                eta_stack.pop()

        return len(eta_stack)