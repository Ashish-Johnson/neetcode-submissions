class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=  ''.join(c for c in s if c.isalnum()).lower()
        string = s[::-1]
        return s == string