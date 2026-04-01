class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join(char.lower() for char in s if char.isalnum())
        return s_clean == s_clean[::-1]