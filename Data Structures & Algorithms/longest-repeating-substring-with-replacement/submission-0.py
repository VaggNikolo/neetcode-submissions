class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l,r=0,0
        maxw=0

        chars=defaultdict(int)

        while r<len(s):
            chars[s[r]]+=1
            res = max(chars[s[r]],res)
            while r-l-res+1>k:
                chars[s[l]]-=1
                l+=1
            maxw = max(maxw,r-l+1)
            r+=1
            

        return maxw
            

