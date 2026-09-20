import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max-heap via negation: the root is the negated heaviest stone
        h: list[int] = [-stone for stone in stones]
        heapq.heapify(h)

        while len(h) > 1:
            neg_y = heapq.heappop(h)  # heaviest stone, negated
            neg_x = h[0]              # second heaviest, negated (peek only)

            if neg_y == neg_x:
                heapq.heappop(h)      # equal weights: both destroyed
            else:
                # x is destroyed and y becomes y - x. In negated form that's
                # neg_y - neg_x, and heapreplace pops neg_x and pushes it in one pass.
                heapq.heapreplace(h, neg_y - neg_x)

        return -h[0] if h else 0