class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind,i in enumerate(nums):
            compl = target - i
            if compl in nums and nums.index(compl)!=ind:
                return sorted([ind, nums.index(compl)])
