class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        for c in s1:
            freq1[ord(c) - ord("a")] += 1

        freq2 = [0] * 26
        matches = sum(1 for x, y in zip(freq1, freq2) if x == y)
        l = 0
        for r, c in enumerate(s2):
            # Add one char to the right of the window
            idx = ord(c) - ord("a")
            matches = self._deltaCheck(freq1, freq2, idx, 1, matches)

            if r - l + 1 == len(s1):
                if matches == 26:
                    return True
                else:
                    # Remove one from the left
                    idx = ord(s2[l]) - ord("a")
                    matches = self._deltaCheck(freq1, freq2, idx, -1, matches)
                    l += 1

        return False

    def _deltaCheck(self, freq1: list, freq2: list, idx: int, delta: int, matches: int) -> int:
        before = freq2[idx] == freq1[idx]
        freq2[idx] += delta
        after = freq2[idx] == freq1[idx]
        if not before and after:
            matches += 1
        elif before and not after:
            matches -= 1
        return matches
