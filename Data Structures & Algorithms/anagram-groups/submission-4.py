class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = dict()

        # for string in strs:
        #     temp_str = "".join(sorted(string))
        #     if temp_str in anagrams:
        #         anagrams[temp_str].append(string)
        #     else:
        #         anagrams[temp_str] = [string]

        # return list(anagrams.values())

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())