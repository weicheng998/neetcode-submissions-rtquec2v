class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack: list = []
        for ind, temp in enumerate(temperatures):
            if not stack or temp <= temperatures[stack[-1]]:
                stack.append(ind)
            else:  # temp > temperatures[stack[-1]]
                while stack and temp > temperatures[stack[-1]]:
                    pre_ind = stack.pop()
                    result[pre_ind] = ind - pre_ind
                stack.append(ind)
        return result
