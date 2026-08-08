# Problem #846: Hand of Straights
# Difficulty : Medium
# Language   : python3
# Runtime    : 31 ms
# Memory     : 21.2 MB
# URL        : https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for num in sorted(hand):
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1

        return True