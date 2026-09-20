class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for ind_w,w in enumerate(words):
            for ind_s,s in enumerate(words):
                if ind_w==ind_s or w.find(s)==-1 or s in res:
                    continue
                res.append(s)
                
        return res