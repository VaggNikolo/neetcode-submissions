class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s=[]
        p=list(zip(position,speed))
        p.sort(reverse=True)

        for i,c in p:
            s.append((target-i)/c)
            if len(s)>=2 and s[-1]<=s[-2]:
                s.pop()
        return len(s)