class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat slow and fast both as pointer starting at ind 0
        slow = nums[0]  # One step
        fast = nums[nums[0]]  # Two steps
        # Floyd's cycle-detection phase 1
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # Floyd's cycle-detection phase 2
        fast = 0
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]
        return nums[slow]
