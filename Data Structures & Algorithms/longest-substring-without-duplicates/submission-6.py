class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        # unique = set()
        unique = {}
        max_len = 0
        
        while r < len(s):
            if s[r] not in unique.keys():
                unique[s[r]] = r
            else:
                l = max(l, unique[s[r]] + 1)
                unique[s[r]] = r

            max_len = max(r - l + 1, max_len)
            r += 1

        return max_len