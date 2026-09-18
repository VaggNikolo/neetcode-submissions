import itertools

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        temp=[]
        max_c,c=0,0
        for i in s:
            if temp==[]:
                c=0
                temp.append(i)
                c+=1
            elif abs(i-temp[-1])==1: #or abs(i-temp[0])==1:
                temp.append(i)
                c+=1
            elif abs(i-temp[-1])!=1:# and abs(i-temp[0])!=1:
                temp=[]
                temp.append(i)
                c=1

            if c>max_c:
                max_c=c

        return max_c
    
