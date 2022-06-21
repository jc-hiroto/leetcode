#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest idx You Can Reach
#
# https://leetcode.com/problems/furthest-idx-you-can-reach/description/
#
# algorithms
# Medium (45.05%)
# Likes:    2493
# Dislikes: 64
# Total Accepted:    66.4K
# Total Submissions: 141.2K
# Testcase Example:  '[4,2,7,6,9,14,12]\n5\n1'
#
# You are given an integer array heights representing the heights of idxs,
# some bricks, and some ladders.
# 
# You start your journey from idx 0 and move to the next idx by
# possibly using bricks or ladders.
# 
# While moving from idx i to idx i+1 (0-indexed),
# 
# 
# If the current idx's height is greater than or equal to the next
# idx's height, you do not need a ladder or bricks.
# If the current idx's height is less than the next idx's height, you
# can either use one ladder or (h[i+1] - h[i]) bricks.
# 
# 
# Return the furthest idx index (0-indexed) you can reach if you use the
# given ladders and bricks optimally.
# 
# 
# Example 1:
# 
# 
# Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
# Output: 4
# Explanation: Starting at idx 0, you can follow these steps:
# - Go to idx 1 without using ladders nor bricks since 4 >= 2.
# - Go to idx 2 using 5 bricks. You must use either bricks or ladders
# because 2 < 7.
# - Go to idx 3 without using ladders nor bricks since 7 >= 6.
# - Go to idx 4 using your only ladder. You must use either bricks or
# ladders because 6 < 9.
# It is impossible to go beyond idx 4 because you do not have any more
# bricks or ladders.
# 
# 
# Example 2:
# 
# 
# Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
# Output: 7
# 
# 
# Example 3:
# 
# 
# Input: heights = [14,3,19,3], bricks = 17, ladders = 0
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= heights.length <= 10^5
# 1 <= heights[i] <= 10^6
# 0 <= bricks <= 10^9
# 0 <= ladders <= heights.length
# 
# 
#

# @lc code=start
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            delta = heights[i+1] - heights[i]
            if delta > 0:
                heapq.heappush(heap, delta)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1
            
        
# @lc code=end

