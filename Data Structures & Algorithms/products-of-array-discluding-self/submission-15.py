class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods=[]
        prd=math.prod(nums)
        if 0 in nums:
            ind_zero = nums.index(0)
            prods=[0]*len(nums)
            no_zeros = nums.copy()
            no_zeros[ind_zero]=1
            prods[ind_zero]=math.prod(no_zeros)
        else:
            for n in nums:
                prods.append(int(prd/n))
        return prods
    
    