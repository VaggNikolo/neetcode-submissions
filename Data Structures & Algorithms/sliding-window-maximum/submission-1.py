import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]

        m_heap =[]

        for i in range(len(nums)):
            heapq.heappush(
                m_heap,
                (-nums[i],i)
            )

            while m_heap[0][1] <= (i-k):
                heapq.heappop(m_heap)
            
            if i>=k-1:
                res.append(-m_heap[0][0])
        return res