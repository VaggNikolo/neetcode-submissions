class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l_ind, r_ind = 0, len(height) - 1
        lmax, rmax = height[l_ind], height[r_ind]
        res = 0
        while l_ind < r_ind:
            if lmax < rmax:
                l_ind += 1
                lmax = max(lmax, height[l_ind])
                res += lmax - height[l_ind]
            else:
                r_ind -= 1
                rmax = max(rmax, height[r_ind])
                res += rmax - height[r_ind]
        return res