class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res: list[list[int]] = []
        path: list[int] = []

        def helper(total: int, start: int) -> None:
            if total == target:
                res.append(path.copy())
                return

            for ind in range(start, len(candidates)):
                num = candidates[ind]
                if total + num > target:
                    break
                
                if ind > start and candidates[ind] == candidates[ind - 1]:
                    continue

                path.append(num)
                helper(total + num, ind + 1)
                path.pop()

        helper(0, 0)
        return res
