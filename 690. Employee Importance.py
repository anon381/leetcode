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



#in java
# class Solution {
#     // Recursive DFS to calculate total importance
#     private int dfs(int id, Map<Integer, Employee> empMap) {
#         Employee emp = empMap.get(id);
#         int imp = emp.importance; // own importance
#         for (int subId : emp.subordinates) {
#             imp += dfs(subId, empMap); // add importance of subordinates
#         }
#         return imp;
#     }

#     public int getImportance(List<Employee> employees, int id) {
#         Map<Integer, Employee> empMap = new HashMap<>();
#         for (Employee emp : employees) {
#             empMap.put(emp.id, emp); // map id to employee
#         }
#         return dfs(id, empMap);
#     }
# }
