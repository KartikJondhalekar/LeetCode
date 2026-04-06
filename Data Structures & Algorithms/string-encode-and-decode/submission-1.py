class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        delim = '#'

        for s in strs:
            encoded_str += str(len(s)) + delim + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        delim = '#'
        i = 0

        while i < len(s):
            num_char = 0
            
            while s[i].isdigit():
                num_char = num_char * 10 + int(s[i])
                i += 1

            if s[i] == delim:
                i += 1
                decoded_str.append(s[i : num_char + i])
                i = num_char + i


        return decoded_str