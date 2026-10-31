class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path: list[int] = []
        res: list[list[int]] = []

        def helper(prev_sum: int, choices_start: int) -> None:
            cur_sum = prev_sum + path[-1] if len(path) > 0 else prev_sum

            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(path.copy())
                return

            for num in nums[choices_start:]:
                path.append(num)
                helper(cur_sum, choices_start)
                path.pop()
                choices_start += 1
                if choices_start >= len(nums):
                    break

        helper(0, 0)
        return res
