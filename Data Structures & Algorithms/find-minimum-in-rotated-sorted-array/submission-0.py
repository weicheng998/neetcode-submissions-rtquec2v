class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right, mid = 0, len(nums) - 1, 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # nums[mid] may be the min, cannot exclude
                right = mid
            else:
                # The drop is to the right of mid
                left = mid + 1
        return nums[mid]
