class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b=nums1,nums2

        if len(nums1)>len(nums2):
            a,b=b,a
        total= len(nums1)+len(nums2)
        

        return binSearch(a,b,total)


        
        
def binSearch(a:List[int],b:List[int], total:int) -> float:
    l,r=0,len(a)-1
    while True:
        half = (total)//2
        i=(l+r)//2
        j= half-i-2

        l_a = a[i] if i>= 0 else float("-infinity")
        r_a = a[i + 1] if (i + 1) < len(a) else float("infinity")
        l_b = b[j] if j >= 0 else float("-infinity")
        r_b = b[j + 1] if (j + 1) < len(b) else float("infinity")

        if l_a<=r_b and l_b <= r_a:
            if total %2:
                return min(r_a,r_b)
            return (max(l_a,l_b)+min(r_a,r_b))/2
        elif l_a > r_b:
            r=i-1
        else:
            l=i+1