import heapq
from itertools import islice
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Problem constraints already guarantee this, just make sure.
        if len(nums) + 1 < k:
            raise ValueError(f"k={k} exceeds len(nums)+1")

        self.k: int = k
        self.h: list[int] = nums[:k]  # copy, so the caller's list isn't reordered
        heapq.heapify(self.h)  # in place, returns None
        for num in islice(nums, k, None):  # tail of nums, no copy
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            # No-op (returns val) unless val is strictly greater than the root
            heapq.heappushpop(self.h, val)
        return self.h[0]
