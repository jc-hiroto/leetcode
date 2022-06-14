#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#
# https://leetcode.com/problems/employee-importance/description/
#
# algorithms
# Medium (64.01%)
# Likes:    1635
# Dislikes: 1249
# Total Accepted:    176.5K
# Total Submissions: 274.3K
# Testcase Example:  '[[1,5,[2,3]],[2,3,[]],[3,3,[]]]\n1'
#
# You have a data structure of employee information, including the employee's
# unique ID, importance value, and direct subordinates' IDs.
# 
# You are given an array of employees employees where:
# 
# 
# employees[i].id is the ID of the i^th employee.
# employees[i].importance is the importance value of the i^th employee.
# employees[i].subordinates is a list of the IDs of the direct subordinates of
# the i^th employee.
# 
# 
# Given an integer id that represents an employee's ID, return the total
# importance value of this employee and all their direct and indirect
# subordinates.
# 
# 
# Example 1:
# 
# 
# Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
# Output: 11
# Explanation: Employee 1 has an importance value of 5 and has two direct
# subordinates: employee 2 and employee 3.
# They both have an importance value of 3.
# Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.
# 
# 
# Example 2:
# 
# 
# Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
# Output: -3
# Explanation: Employee 5 has an importance value of -3 and has no direct
# subordinates.
# Thus, the total importance value of employee 5 is -3.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= employees.length <= 2000
# 1 <= employees[i].id <= 2000
# All employees[i].id are unique.
# -100 <= employees[i].importance <= 100
# One employee has at most one direct leader and may have several
# subordinates.
# The IDs in employees[i].subordinates are valid IDs.
# 
# 
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {}
        self.res = 0
        for e in employees:
            emap[e.id] = e
        print(emap)
        def helper(emp):
            self.res += emp.importance
            if len(emp.subordinates) == 0:
                return
            for sub in emp.subordinates:
                helper(emap[sub])
        helper(emap[id])
        return self.res
# @lc code=end

