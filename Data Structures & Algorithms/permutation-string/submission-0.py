class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # Translate s1 into list of freq
        freq1 = [0] * 26  # 26 lowercase letters
        for c in s1:
            freq1[ord(c) - ord('a')] += 1

        l = 0
        freq2 = [0] * 26
        for r, c in enumerate(s2):
            freq2[ord(c) - ord('a')] += 1
            win_len = r - l + 1
            if win_len == len(s1):
                if freq2 == freq1:
                    return True
                else:
                    freq2[ord(s2[l]) - ord('a')] -= 1
                    l += 1
        
        return False
        