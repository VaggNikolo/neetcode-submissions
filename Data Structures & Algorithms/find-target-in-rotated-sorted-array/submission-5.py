class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<r:
            m = (l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        pivot=l

        def bin_search(l:int,r:int)->int:
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    return m
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return -1

        l_res=bin_search(0,pivot-1)
        if l_res!=-1:
            return l_res

        r_res = l_res=bin_search(pivot,len(nums)-1)

        return r_res