class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while numbers[i]+numbers[j]!=target:
            if numbers[j]>target-numbers[i]:
                j-=1
            elif numbers[j]<target-numbers[i]:
                j=len(numbers)-1
                i+=1
                continue
        return [i+1,j+1]