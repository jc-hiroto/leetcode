#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}
        res = 0
        while d:
            # print(d)
            x, y = min(d, key=d.get) # returns the key of the min value element.
            # print(x,y)
            res += d.pop((x, y))
            for x1, y1 in d:
                d[(x1, y1)] = min(d[(x1, y1)], abs(x - x1) + abs(y - y1))
        return res
# @lc code=end
