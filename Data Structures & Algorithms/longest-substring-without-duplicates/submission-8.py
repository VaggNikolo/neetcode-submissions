class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml=0
        sub=''
        for c in s:
            if c in sub:
                sub=sub.rsplit(c)[1]
            sub+=c
            ml=max(len(sub),ml)
            

        return ml