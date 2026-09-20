import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Build a heap of stone weights
        h: list[int] = [-1 * stone for stone in stones]
        heapq.heapify(h)

        # Simulate until no more than one stone
        while len(h) > 1:
            s1 = heapq.heappop(h)
            s2 = heapq.heappop(h)

            if s1 == s2:
                # Both destroyed
                continue

            heapq.heappush(h, s1 - s2)

        return -1 * h[0] if bool(h) else 0
