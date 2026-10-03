class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        c,n=0,len(matrix)-1

        if n==c:
            return binSearchInRow(matrix[n],target)

        while c<=n:
            m = c + (n-c)//2
            if matrix[m][-1]<target:
                c=m+1
            elif matrix[m][0]>target:
                n=m-1
            else:
                return binSearchInRow(matrix[m],target)
        return False
            

def binSearchInRow(a: List[int], target: int) -> bool:
    l,r=0,len(a)-1

    if l==r:
        return a[l]==target

    while l<=r:
        m = l + (r-l)//2
        if a[m]<target:
            l=m+1
        elif a[m]>target:
            r=m-1
        else:
            return True
    return False