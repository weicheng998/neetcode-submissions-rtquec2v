class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def helper(idx: int, path: List[int]) -> None:
            if idx >= len(nums):
                res.append(path.copy())
                return
            helper(idx + 1, path)  # Skip
            path.append(nums[idx])
            helper(idx + 1, path)  # Take
            path.pop()

        res: List[List[int]] = []
        helper(0, [])
        return res
