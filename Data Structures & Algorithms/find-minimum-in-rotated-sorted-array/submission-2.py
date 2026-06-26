class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, mid = 0, len(nums) - 1, 0
        while l <= r:
            if nums[l] < nums[r]:
                # Fully sorted, no rotation
                return nums[l]

            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] > nums[l]:
                l = mid + 1
            else:  # nums[mid] == nums[l]
                # Only if two elements left and mid == l
                return min(nums[l], nums[r])
        return nums[mid]
