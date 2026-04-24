class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = list(s)
        s2 = list(t)
        s1.sort()
        s2.sort()
        for i in range(0,len(s)):
            if s1[i] != s2[i]:
                    return False
        return True

        