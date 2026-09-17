class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sd,td = {},{}
        #lambda x,d: d[c]+=1 for c in x 
        return Counter(s)==Counter(t)
        # for c in s:
        #     if c in sd.keys():
        #         sd[c]+=1
        #     else:
        #         sd[c]=1
        # for c in t:
        #     if c in td.keys():
        #         td[c]+=1
        #     else:
        #         td[c]=1
        # if td==sd:
        #     return True
        # return False