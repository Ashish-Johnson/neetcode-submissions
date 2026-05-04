class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=  ''.join(c for c in s if c.isalnum()).lower()
        string = s[::-1]
        if s == string:
            return True
        else:
            return False