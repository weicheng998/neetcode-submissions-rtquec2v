import heapq
import math
from itertools import islice


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max heap tracking the k closet points.
        h: list[tuple[float, list]] = [(-(x * x + y * y), [x, y]) for x, y in points[:k]]
        heapq.heapify(h)
        # Push the rest of the points into the heap.
        # A point closer to the origin, its neg_dist larger.
        for x, y in islice(points, k, None):
            heapq.heappushpop(h, (-(x * x + y * y), [x, y]))
        return [l for _, l in h]