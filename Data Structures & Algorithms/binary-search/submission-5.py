class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]<target:
                l=m+1
                m=int(math.floor((r-m)/2))
            elif nums[m]>target:
                r=m-1
                m=int(math.floor((m-l)/2))  
            elif nums[m]==target:
                return m  
        return -1