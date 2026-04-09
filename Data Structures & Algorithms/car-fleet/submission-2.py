class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        eta_stack = []

        for p, s in sorted(pairs)[::-1]:
            eta_stack.append((target - p) / s)
            if len(eta_stack) >=2 and eta_stack[-1] <= eta_stack[-2]:
                eta_stack.pop()

        return len(eta_stack)