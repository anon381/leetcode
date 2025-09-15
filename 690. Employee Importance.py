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
        def dfs(emp):
            imp = emps[emp].importance            
            for s in emps[emp].subordinates:
                imp += dfs(s)
            return imp
        
        emps= {emp.id: emp for emp in employees}
        
        return dfs(id)
        
