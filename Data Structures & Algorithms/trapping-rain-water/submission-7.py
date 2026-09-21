class Solution:
    def trap(self, height: List[int]) -> int:
        v=0
        l,r = 0,len(height)-1
        l_max,r_max = height[l], height[r]
        while l<r:
            if height[l]<height[r]:
                if height[l]>=l_max:
                    l_max=height[l]
                else:
                    v+=l_max-height[l]
                l+=1
            else:
                if height[r]>=r_max:
                    r_max=height[r]
                else:
                    v+=r_max-height[r]
                r-=1
        return v  
