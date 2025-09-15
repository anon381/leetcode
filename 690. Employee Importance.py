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
        
#in cpp
# class Solution {
# public:
#     int getImportance(vector<Employee*> employees, int id) {
#         unordered_map<int, Employee*>m;
#         for(auto x: employees) m[x->id] = x;
#         int sum = 0;
#         DFS(m, id, sum);
#         return sum;
#     }
    
#     void DFS(unordered_map<int, Employee*>& m, int id, int& sum){
#         sum += m[id]->importance;
#         for(auto x: m[id]->subordinates) DFS(m, x, sum);
#     }
# };
