class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        i,j=0,1
        msum=nums[i]

        while j<len(nums):
            print(i,j,msum)
            if nums[j]>nums[j-1]:
                msum=max(msum,sum(nums[i:j+1]))
            else:
                i=j
            j+=1
        return msum