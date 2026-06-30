class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_len = 0
        char_set = set()
        l = 0
        for r in range(len(s)):
            if s[r] not in char_set:
                char_set.add(s[r])
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                while s[l] != s[r] and l < r:
                    char_set.remove(s[l])
                    cur_len -= 1
                    l += 1
                l += 1
        return max_len
