# Problem #49: Group Anagrams
# Difficulty : Medium
# Language   : python3
# Runtime    : 11 ms
# Memory     : 21.9 MB
# URL        : https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for string in strs:
            temp_str = "".join(sorted(string))
            if temp_str in anagrams:
                anagrams[temp_str].append(string)
            else:
                anagrams[temp_str] = [string]

        return list(anagrams.values())