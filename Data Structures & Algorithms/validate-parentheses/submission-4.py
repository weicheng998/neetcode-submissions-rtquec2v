class Solution:
    def isValid(self, s: str) -> bool:
        c_map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []

        for char in s:
            if char not in c_map:
                stack.append(char)
            else:
                if not stack or c_map[char] != stack.pop():
                    return False
        if stack:
            return False
        return True