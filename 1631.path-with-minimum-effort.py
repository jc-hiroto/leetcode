#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
from collections import deque
import heapq
import math


class Solution:
    '''
        # BFS Solution
        # Time: O(m ^ 2 * n ^ 2), space: O(m * n).
        def minimumEffortPath(self, heights: List[List[int]]) -> int:
            m, n = len(heights), len(heights[0])
            ef = [[math.inf] * n for _ in range(m)]
            ef[0][0] = 0
            dq = deque([(0, 0)])
            while dq:
                x, y = dq.popleft()
                for r, c in (x, y+1), (x+1, y), (x, y-1), (x-1, y):
                    if m > r >= 0 and n > c >= 0:
                        next_ef = max(ef[x][y], abs(heights[x][y] - heights[r][c]))
                        if next_ef < ef[r][c]:
                            ef[r][c] = next_ef
                            dq.append((r, c))
            return ef[-1][-1]
    '''
    # Djikstra solution
    # Time: O(m * n log(m * n)), space: O(m * n), where m and n are the dimensions of the matrix.
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        efs = [[math.inf] * n for _ in range(m)]
        efs[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            ef, x, y = heapq.heappop(heap)
            if (x, y) == (m - 1, n - 1):
                return ef
            for r, c  in (x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y):
                if m > r >= 0 <= c < n:
                    next_ef = max(efs[x][y], abs(heights[x][y] - heights[r][c]))
                    if next_ef < efs[r][c]:
                        efs[r][c] = next_ef
                        heapq.heappush(heap, (next_ef, r, c))
            
    # @lc code=end