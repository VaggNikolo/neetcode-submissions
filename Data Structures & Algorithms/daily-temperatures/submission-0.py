class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0]*len(temperatures)

        for ind,i in enumerate(temperatures):

            while s and s[-1][1]<i:
                n = s.pop()
                res[n[0]]=ind-n[0]
            s.append((ind,i))

                

        return res
        