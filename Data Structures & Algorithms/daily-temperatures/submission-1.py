class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result: list[int] = [0] * len(temperatures)
        stack: list[int] = []

        ind = 0
        while ind < len(temperatures):
            while stack and temperatures[ind] > temperatures[stack[-1]]:
                pre_ind = stack.pop()
                result[pre_ind] = ind - pre_ind
            stack.append(ind)
            ind += 1
        
        return result