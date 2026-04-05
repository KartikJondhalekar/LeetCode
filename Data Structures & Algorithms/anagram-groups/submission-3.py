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