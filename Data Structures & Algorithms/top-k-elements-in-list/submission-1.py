class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=Counter(nums).most_common(k)
        l=[i[0] for i in l]
        return l