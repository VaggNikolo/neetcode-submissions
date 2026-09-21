class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=[]
        p=0
        for i in prices:
            if not s:
                s.insert(0,i)
                continue
            elif i<s[-1]:
                if i<s[0] and len(s)>=2 and s[-1]-s[0]>p:
                    p = s[-1]-s[0]
                    s=[]
                    s.insert(0,i)
                elif i<s[0]:
                    s[0]=i
                    continue  
            elif i>s[-1]:
                s.append(i)
        
        return max(p,s[-1]-s[0])
