from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # math trick problem, not traveling sales man problem
        res = 0
        n = len(points)
        for i in range(n - 1):
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[i + 1][0], points[i + 1][1]
            res += max(abs(y2 - y1), abs(x2 - x1))

        return res
