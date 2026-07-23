class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = [0] * 26
        max_freq = 0
        max_win = 0
        l = 0

        for r, c in enumerate(s):
            win_size = r - l + 1
            char_freq[ord(c) - ord("A")] += 1
            max_freq = max(max_freq, char_freq[ord(c) - ord("A")])
            if win_size - max_freq > k:
                char_freq[ord(s[l]) - ord("A")] -= 1
                l += 1
            else:
                max_win = max(max_win, win_size)

        return max_win
