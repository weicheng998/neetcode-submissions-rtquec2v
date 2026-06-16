class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_map: dict = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        stack: list = []
        for token in tokens:
            if token in op_map:
                b = stack.pop()
                a = stack.pop()
                result = op_map[token](a, b)
                stack.append(result)
            else:
                stack.append(int(token))
        
        if len(stack) != 1:
            raise ValueError("Invalid expression")
        return stack.pop()
