class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        unique = set()
        max_len = 0
        
        while r < len(s):
            if s[r] not in unique:
                curr_len = r - l + 1
                unique.add(s[r])
                max_len = max(curr_len, max_len)
            else:
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1

                unique.add(s[r])

            r += 1

        return max_len