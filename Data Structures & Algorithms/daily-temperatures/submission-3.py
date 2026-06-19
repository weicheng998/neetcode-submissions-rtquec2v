class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result: list[int] = [0] * len(temperatures)
        stack: list[int] = []

        for ind, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                pre_ind = stack.pop()
                result[pre_ind] = ind - pre_ind
            stack.append(ind)

        return result
