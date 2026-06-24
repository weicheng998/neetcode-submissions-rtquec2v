class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_k = right

        while left <= right:
            k = (left + right) // 2
            time_finish = sum([(pile + k - 1) // k for pile in piles])
            if time_finish <= h:
                min_k = k
                right = k - 1
            else:
                left = k + 1

        return min_k
