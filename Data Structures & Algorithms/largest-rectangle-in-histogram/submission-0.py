class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prev_smaller = left_min(heights)
        next_smaller = right_min(heights)

        max_area = 0

        for i in range(len(heights)):
            width = next_smaller[i] - prev_smaller[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area


def left_min(l: List[int]):
    n = len(l)
    prev_smaller = [-1] * n
    s = []

    for i in range(n):
        while s and l[i] <= l[s[-1]]:
            s.pop()

        if s:
            prev_smaller[i] = s[-1]

        s.append(i)

    return prev_smaller


def right_min(l: List[int]):
    n = len(l)
    next_smaller = [n] * n
    s = []

    for i in range(n - 1, -1, -1):
        while s and l[i] <= l[s[-1]]:
            s.pop()

        if s:
            next_smaller[i] = s[-1]

        s.append(i)

    return next_smaller