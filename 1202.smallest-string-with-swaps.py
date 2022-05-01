#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#

# @lc code=start
from collections import defaultdict


class Solution:
    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Use union-find to find the root of each pair 
        # Then sort each group by the root of each pair 
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.union(a, b)
        
        group = defaultdict(lambda: ([],[]))
        for i, ch in enumerate(s):
            parent = self.find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)
        res = [''] * len(s)
        for idx, chars in group.values():
            chars.sort()
            for i, ch in zip(idx, chars):
                res[i] = ch
        return ''.join(res)
# @lc code=end

