class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = "".join([char.lower() for char in s if char.isalnum()])
        return s_cleaned == s_cleaned[::-1]