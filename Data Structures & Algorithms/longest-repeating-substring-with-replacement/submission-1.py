class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_len = 0
        max_window_len = 0
        window_char_freq = [0] * 26  # Only uppercase english characters
        l = 0

        for r, c in enumerate(s):
            window_char_freq[ord(c) - ord("A")] += 1
            window_len = r - l + 1
            if window_len - max(window_char_freq) > k:
                window_char_freq[ord(s[l]) - ord("A")] -= 1
                l += 1
            else:
                max_window_len = max(max_window_len, window_len)

        return max_window_len
