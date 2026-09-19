import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        if len(nums) + 1 < k:
            raise ValueError

        self.k: int = k
        self.h: list[int] = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            # Build the foundation heap of size k
            heapq.heappush(self.h, val)
        else:
            if val > self.h[0]:
                heapq.heappushpop(self.h, val)
        return self.h[0]
