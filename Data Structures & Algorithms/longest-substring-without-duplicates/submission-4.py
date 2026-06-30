class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        char_set = set()
        for r in range(len(s)):
            if s[r] not in char_set:
                max_len = max(max_len, r - l + 1)
            else:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
            char_set.add(s[r])
        return max_len
