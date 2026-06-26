class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                # nums[mid] may be the min, cannot exclude
                r = mid
            else:
                # The drop is to the right of mid
                l = mid + 1
        return nums[l]
