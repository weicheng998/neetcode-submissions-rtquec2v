class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res: list[list[int]] = []
        path: list[int] = []

        def helper(total: int, start: int) -> None:
            if total == target:
                res.append(path.copy())
                return

            for ind in range(start, len(nums)):
                num = nums[ind]
                if total + num > target:
                    break  # sorted: every later candidate overshoots too

                path.append(num)
                helper(total + num, ind)  # ind, not ind + 1: reuse allowed
                path.pop()

        helper(0, 0)
        return res