class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0]*len(temperatures)
        for ind,i in enumerate(temperatures):
            while s and s[-1][1]<i:
                n,_ = s.pop()
                res[n]=ind-n
            s.append((ind,i))
        return res
        