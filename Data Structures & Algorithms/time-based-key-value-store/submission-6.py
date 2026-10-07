class TimeMap:

    def __init__(self):
        self.d={}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]=[]
        self.d[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, v = "", self.d.get(key, [])
        l,r=0,len(v)-1

        while l<=r:
            m = (r+l)//2

            if v[m][1]<=timestamp:
                res=v[m][0]
                l=m+1
            else:
                r=m-1
        return res