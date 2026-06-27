class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            if nums[mid] < nums[r]:
                # Mid to right is the smaller side
                if nums[mid] < target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:  # nums[mid] >= nums[r]
                # Mid to right includes the drop, unsorted
                if nums[l] < target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
