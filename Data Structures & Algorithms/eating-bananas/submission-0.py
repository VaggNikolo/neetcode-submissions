class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<=r:
            k=(l+r)//2
            if canEatInTime(piles,k,h):
                r=k-1
            else:
                l = k+1
        return l

def canEatInTime(piles: List[int], eatRate: int, h: int) -> bool:
    hours = 0

    for pile in piles:
        hours += (pile + eatRate - 1) // eatRate
        if hours > h:
            return False

    return True