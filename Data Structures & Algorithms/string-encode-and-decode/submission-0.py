class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        st = ''
        for s in strs:
            st += str(len(s))+'*'+s
        return st

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        st = []
        i=0
        while i < len(s):
            j = i

            while s[j] != '*':
                j +=1
            
            length = int(s[i:j])
            word = s[j+1 : j+1+length]

            st.append(word)

            i = j + 1 + length
        return st





