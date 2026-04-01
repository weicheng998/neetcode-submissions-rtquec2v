class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for s in strs:
            encoded_s = str(len(s)) + "#" + s
            encoded_list.append(encoded_s)
        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            # 1. Read the length of the cur chunk
            cur_len = []
            while s[i] != "#":
                cur_len.append(s[i])
                i += 1
            cur_len = int("".join(cur_len))
            # 2. Skip the "#"
            i += 1
            # 3. Read the string
            cur_s = []
            for j in range(cur_len):
                cur_s.append(s[i])
                i += 1
            cur_s = "".join(cur_s)
            decoded_list.append(cur_s)
        return decoded_list
