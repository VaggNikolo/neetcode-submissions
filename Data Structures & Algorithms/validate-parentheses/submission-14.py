class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            '[':']',
            '(':')',
            '{':'}'
        }
        st=[]

        for c in s:
            print(c,st)
            if (not st):
                st.append(c)
                continue
            if m.get(st[-1],'')==c:
                st.pop(-1)
            else:
                st.append(c)
        
        return st==[] 
            
            

        