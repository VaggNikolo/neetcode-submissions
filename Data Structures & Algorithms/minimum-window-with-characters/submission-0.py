class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s) or t=="":
            return ""

        count_s = [0]*256
        count_t = [0]*256

        for c in t:
            count_t[ord(c)]+=1
        
        start,start_idx,min_len,count = 0,-1,float('inf'),0

        for i in range(len(s)):
            count_s[ord(s[i])]+=1
        
            if count_t[ord(s[i])] != 0 and count_s[ord(s[i])] <= count_t[ord(s[i])]:
                count+=1
            
            if count == len(t):
                while count_s[ord(s[start])] > count_t[ord(s[start])] or count_t[ord(s[start])]==0:
                    if count_s[ord(s[start])]>count_t[ord(s[start])]:
                        count_s[ord(s[start])]-=1
                    start+=1

                length=i-start+1
                if min_len>length:
                    min_len=length
                    start_idx=start
        
        if start_idx == -1:
            return ""

        return s[start_idx:start_idx + min_len]
