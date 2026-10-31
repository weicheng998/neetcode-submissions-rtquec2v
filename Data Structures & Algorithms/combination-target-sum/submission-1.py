class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res: list[list[int]] = []
        path: list[int] = []

        def helper(total: int, start: int) -> None:
            if total > target:
                return
            if total == target:
                res.append(path.copy())
                return

            for ind in range(start, len(nums)):
                num = nums[ind]
                total += num
                path.append(num)
                helper(total, ind)
                total -= num
                path.pop()

        helper(0, 0)
        return res
