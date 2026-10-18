class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: list[list[int]] = []
        path: list[int] = []

        def helper(idx: int) -> None:
            if idx >= len(nums):
                res.append(path.copy())
                return
            helper(idx + 1)  # Skip
            path.append(nums[idx])
            helper(idx + 1)  # Take
            path.pop()

        helper(0)
        return res
