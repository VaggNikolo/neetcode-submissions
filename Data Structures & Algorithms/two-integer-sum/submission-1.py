from functools import reduce
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = [(x + y, i, j) for i,x in enumerate(nums) for j,y in enumerate(nums) if i!=j]
        
        sol = [(l[1],l[2]) for l in sums if l[0]==target]

        sol = list(sorted(set(reduce(lambda x,y:x+y, sol))))


        print(sol)
        return sol
