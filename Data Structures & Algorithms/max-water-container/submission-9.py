class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        max_v=0
        while i<j:
            if calculateVolume(i,j,heights[i], heights[j])>max_v:
                max_v=calculateVolume(i,j,heights[i], heights[j])
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_v
        
def calculateVolume(x1:int,x2:int,y1:int,y2:int) -> int:
    return abs(x2-x1)*min(y1,y2)