import heapq
from itertools import islice


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h: list[int] = nums[:k]
        heapq.heapify(h)
        for num in islice(nums, k, None):
            heapq.heappushpop(h, num)
        return h[0]
