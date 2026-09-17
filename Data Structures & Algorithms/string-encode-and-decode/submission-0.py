class Solution:

    def encode(self, strs: List[str]) -> str:
        l=[]
        s=''
        for i in strs:
            l.append(len(i))
            s+=i
        return s+(str(l))
    def decode(self, s: str) -> List[str]:
        res=[]
        l=eval('['+s.rsplit('[',1)[1])
        curr=0
        for n in l:
            print(n)
            res.append(s[curr:curr+int(n)])
            curr+=n
        return res
