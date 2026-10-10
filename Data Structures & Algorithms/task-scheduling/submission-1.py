from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks).values()
        max_freq = max(freqs)
        num_max = sum(1 for freq in freqs if freq == max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + num_max)