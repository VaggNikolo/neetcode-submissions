class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol={}
        res=[]
        s = [(s,sorted(Counter(s).elements())) for s in strs]
        for i in s:
            if tuple(i[1]) not in sol.keys():
                sol[tuple(i[1])]=[(i[0])]
            else:
                sol[tuple(i[1])].append((i[0]))
        for k in sol.keys():
            res.append(sol[k])
        return res